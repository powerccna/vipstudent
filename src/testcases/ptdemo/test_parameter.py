#!/usr/bin/env python
# encoding: utf-8

import pytest
import random

@pytest.mark.parametrize("x", [(1),(2),(6)])
def test_add(x):
    print(x)
    assert x == random.randrange(1,7)

