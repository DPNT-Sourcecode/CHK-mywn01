import pytest

from lib.solutions.hello import hello

@pytest.mark.parametrize('friend, expected', [
    ('Barry', 'Barry'),
    ('Lucy', 'Lucy'),
    ('norman', 'Norman'),
    ('edgar ALLeN pOE', 'Edgar Allen Poe'),
])
def test_hello(friend, expected):
    h = hello(friend)
    assert h == "Hello, {}!".format(expected)
