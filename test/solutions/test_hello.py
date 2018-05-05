import pytest

from lib.solutions.hello import hello

def test_hello():
    h = hello('Barry')
    assert isinstance(h, str)
