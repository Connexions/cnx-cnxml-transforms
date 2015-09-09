# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2013, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
import os

from cnxarchive.tests.testing import (
    data_fixture, db_connect, schema_fixture
    )


__all__ = (
    'DATA_DIRECTORY',
    'data_fixture',
    'db_connect',
    'schema_fixture',
    )


here = os.path.abspath(os.path.dirname(__file__))
DATA_DIRECTORY = os.path.join(here, 'data')
