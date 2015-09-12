# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2013, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
import os
import re

from cnxarchive.tests.testing import (
    data_fixture, db_connect, schema_fixture, db_connection_factory
    )
import psycopg2.extras


__all__ = (
    'DATA_DIRECTORY',
    'data_fixture',
    'db_connect',
    'schema_fixture',
    'FauxPlpy',
    )


here = os.path.abspath(os.path.dirname(__file__))
DATA_DIRECTORY = os.path.join(here, 'data')


class FauxPlpy(object):
    @classmethod
    def cursor(cls):
        db_connect = db_connection_factory()
        return db_connect().cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

    @classmethod
    def prepare(cls, stmt, field_types):
        return FauxPlpyStatement(stmt, field_types)

    @classmethod
    def execute(cls, stmt, args, nrows=None):
        with cls.cursor() as cursor:
            return stmt.execute(cursor, args)


class FauxPlpyStatement(object):
    def __init__(self, stmt, field_types):
        stmt = re.sub('\$[0-9]+', '%s', stmt)
        self.stmt = stmt
        self.field_types = field_types

    def execute(self, cursor, args):
        args = list(args)
        for i, field_type in enumerate(self.field_types):
            if field_type == 'bytea':
                args[i] = memoryview(args[i])
        cursor.execute(self.stmt, args)
        cursor.connection.commit()
        if (cursor.statusmessage.startswith('SELECT') or
                'returning' in cursor.query.lower()):
            return cursor.fetchall()
