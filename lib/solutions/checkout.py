# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
from .product import products



def total_price(skus):
    pass

def extract_skus(skus):
    counter = Counter(skus)
    for k in counter.keys():
        if k not in products:
            raise ValueError('Invalid SKUs.')
    return dict(counter)

def checkout(skus):
    try:
        skus = extract_skus(skus)
    except ValueError:
        return -1
    for p in VALID_PRODUCTS:
        if p not in skus:
            skus[p] = 0
    cost = total_price(
        skus['A'],
        skus['B'],
        skus['C'],
        skus['D'],
        skus['E'],
        skus['F'],
    )
    return cost
