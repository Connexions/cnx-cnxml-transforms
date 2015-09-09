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
import psycopg2


__all__ = (
    'DATA_DIRECTORY',
    'data_fixture',
    'db_connect',
    'schema_fixture',
    )


here = os.path.abspath(os.path.dirname(__file__))
DATA_DIRECTORY = os.path.join(here, 'data')


class FakePlpy(object):
    @staticmethod
    def prepare(stmt, param_types):
        return FakePlpyPlan(stmt)

    @staticmethod
    def execute(plan, args, rows=None):
        return plan.execute(args, rows=rows)


fake_plpy = FakePlpy()


class FakePlpyPlan(object):
    def __init__(self, stmt):
        self.stmt = re.sub(
            '\$([0-9]+)', lambda m: '%(param_{})s'.format(m.group(1)), stmt)

    def execute(self, args, rows=None):
        connect = db_connection_factory()
        with connect() as db_conn:
            with db_conn.cursor(
                    cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                params = {}
                for i, value in enumerate(args):
                    params['param_{}'.format(i + 1)] = value
                cursor.execute(self.stmt, params)
                try:
                    results = cursor.fetchall()
                    if rows is not None:
                        results = results[:rows]
                    return results
                except psycopg2.ProgrammingError as e:
                    if e.message != 'no results to fetch':
                        raise
