#!/usr/bin/env python
# encoding: utf-8
import pytest


@pytest.fixture(scope='session',autouse=True)
#@pytest.fixture(scope='session')
def build_db_connection():
    print('building database connection')
    yield
    print('close database connection')