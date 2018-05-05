import pytest

from lib.solutions.checkout import checkout, extract_skus, apply_pricing

@pytest.mark.parametrize('skus, expected', [
    ('A', {'A': 1}),
    ('AB', {'A': 1, 'B': 1}),
    ('2AB', {'A': 2, 'B': 1}),
    ('2A3C', {'A': 2, 'C': 3}),
    ('2A3D2A', {'A': 4, 'D': 3}),
    pytest.param('3E', {}, marks=pytest.mark.xfail(raises=ValueError)),
    pytest.param('A3', {}, marks=pytest.mark.xfail(raises=ValueError)),
    pytest.param('Et tu, Brute?', {}, marks=pytest.mark.xfail(raises=ValueError))
])
def test_extract_skus(skus, expected):
    extract = extract_skus(skus)
    assert extract == expected


@pytest.mark.parametrize('item_quanties, expected', [
    ({'A': 1}, {'A': 50}),
    ({'A': 1, 'B': 1}, {'A': 50, 'B': 30}),
    ({'A': 2, 'B': 1}, {'A': 100, 'B': 30}),
    ({'A': 4, 'D': 3}, {'A': 180, 'D': 45})

])
def test_apply_pricing(item_quanties, expected):
    prices = apply_pricing(item_quanties)
    assert prices == expected

@pytest.mark.parametrize('skus, price_expected', [
    ('A', 50),
    ('1A', 50),
    ('3A', 130),
    ('4A', 180),
    ('6A', 260),
    ('7A', 310),
    ('B', 30),
    ('2B', 45),
    ('3B', 75),
    ('4B', 90),
    ('C', 20),
    ('2C', 40),
    ('3C', 60),
    ('D', 15),
    ('2D', 30),
    ('1A1A', 100),
    ('AB', 80),
    ('1A1B', 80),
    ('2AC', 120),
    ('3AC', 150),
])
def test_checkout(skus, price_expected):
    price = checkout(skus)
    assert price == price_expected
