import pytest

from lib.solutions.checkout import (checkout, extract_skus, group_discount_cost)
from lib.solutions.product import *


@pytest.mark.parametrize('skus, expected', [
    ({'A': 1}, 0),
    ({'S': 1}, 20),
    ({'S': 3}, 45),
    ({'S': 2, 'T': 1}, 45),
    ({'S': 2, 'T': 2}, 65),
    ({'S': 2, 'T': 3}, 85),
    ({'S': 2, 'T': 3, 'X': 1}, 90),
    ({'S': 2, 'T': 3, 'X': 2}, 107),
])
def test_group_discount_cost(skus, expected):
    assert group_discount_cost(skus) == expected


@pytest.mark.parametrize('discounted_product, item_quantities, expected', [
    (A, {'A': 1}, 50),
    (B, {'A': 1}, 0),
    (B, {'B': 2}, 45),
    (A, {'A': 6, 'B': 2}, 250),
    (Q, {'Q': 1}, 30),
    (Q, {'Q': 3}, 80),
    (Q, {'Q': 3, 'R': 2}, 80),
    (Q, {'Q': 3, 'R': 3}, 60),

])
def test_get_price(discounted_product, item_quantities, expected):
    assert discounted_product.get_price(item_quantities) == expected



@pytest.mark.parametrize('skus, expected', [
    ('A', {'A': 1}),
    ('AB', {'A': 1, 'B': 1}),
    ('AB', {'A': 1, 'B': 1}),
    ('AACCC', {'A': 2, 'C': 3}),
    ('AAAADDD', {'A': 4, 'D': 3}),
    pytest.param('3E', {}, marks=pytest.mark.xfail(raises=ValueError)),
    pytest.param('A3', {}, marks=pytest.mark.xfail(raises=ValueError)),
    pytest.param('Et tu, Brute?', {}, marks=pytest.mark.xfail(raises=ValueError))
])
def test_extract_skus(skus, expected):
    extract = extract_skus(skus)
    assert extract == expected

@pytest.mark.parametrize('skus, price_expected', [
    ('A', 50),
    ('AA', 100),
    ('AAA', 130),
    ('AAAA', 180),
    ('B', 30),
    ('C', 20),
    ('D', 15),
    ('AB', 80),
    ('ABCDABCD', 215),
    ('E', 40),
    ('EE', 80),
    ('BEE', 80),
    ('BBEE', 110),
    ('BBBBEE', 155),
    ('BBBBEEEE', 205),
    ('F', 10),
    ('FF', 20),
    ('FFF', 20),
    ('FFFF', 30),
    ('FFFFFF', 40),
    ('AAABBQQRRRZ', 376),
    ('UUU', 120),
    ('UUUU', 120),
    ('UUUUUU', 200),
    ('XXX', 45),
    ('XXXX', 62),
    ('TTTT', 65),
    ('AAASTX', 175),
])
def test_checkout(skus, price_expected):
    price = checkout(skus)
    assert price == price_expected
