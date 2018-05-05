import pytest

from lib.solutions.sum import sum

@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (0, 0, 0),
    (99, 99, 198),
])
def test_sum(a, b, expected):
    assert sum(a, b) == expected
