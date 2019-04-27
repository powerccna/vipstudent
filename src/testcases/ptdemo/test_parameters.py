#!/usr/bin/env python
# encoding: utf-8

import pytest

@pytest.mark.parametrize("x,y", [
    (3+5, 9),
    (2+4, 6),
    (6*9, 42),
    ("testerhome", "testerhome"),
])

def test_add(x, y):
    assert x == y


@pytest.mark.parametrize("x,y,z", [
    (3+5, 9,8),
    (2+4, 6,9),
    (6*9, 42,9),
    ("testerhome", "testerhome","new"),
])

def test_multiple_add(x, y,z):
    assert x == y+z



@pytest.mark.parametrize("x,y", [
    (9, 9),
    (2, 2),
    (42, 42),
    ("testerhome", "testerhome"),
])
def test_add2(x,y):
    assert x == y