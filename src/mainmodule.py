#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin

import pytest
pytest.main(['-v', '--instafail', 'testcases/api/test_example.py', '-m=P2'])