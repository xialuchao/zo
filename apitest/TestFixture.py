# -*- coding=utf-8 -*-
__author__ = 'Shylock'
__time__ = '2020/03/19'

import pytest

@pytest.fixture()
def test1():
    print("\n start function")

def test_a(test1):
    print("----test a-----")

def TestCase(object):

    def test_b(self, test1):
        print("------test b------")