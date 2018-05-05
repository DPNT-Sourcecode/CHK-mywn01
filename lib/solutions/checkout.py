# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter

VALID_PRODUCTS = ['A', 'B', 'C', 'D', 'E']


def total_price(na, nb, nc, nd, ne):


def extract_skus(skus):
    counter = Counter(skus)
    for k in counter.keys():
        if k not in VALID_PRODUCTS:
            raise ValueError('Invalid SKUs.')
    return dict(counter)

def checkout(skus):
    try:
        skus = extract_skus(skus)
    except ValueError:
        return -1
    prices = apply_pricing(skus)
    return sum(prices.values())
