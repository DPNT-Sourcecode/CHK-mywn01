import pytest

from lib.solutions.checkout import (checkout, extract_skus)
from lib.solutions.product import DiscountedProduct

@pytest.fixture
def discounted_product(request):
    return DiscountedProduct(*request.param)


@pytest.mark.parametrize('discounted_product, expected', [
    (['A', 50, ((3, 130), (5, 200))], 50),
], indirect=['discounted_product'])
def test_get_price(discounted_product, expected):
    assert discounted_product.get_price({'A': 1}) == expected



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
])
def test_checkout(skus, price_expected):
    price = checkout(skus)
    assert price == price_expected
