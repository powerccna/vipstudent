#! /usr/bin/env python
#coding=utf-8

import pytest
def test_multiple_assert():
    pytest.assume(1==2)
    pytest.assume(2 == 2)
    pytest.assume(3 == 2)

    # assert  1==2
    # assert  2==2