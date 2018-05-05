# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
from .product import products



def total_price(skus):
    cost = 0
    for p in products:
        product = products[p]
        cost += product.get_price(skus)
    return cost

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
    for p in products:
        if p not in skus:
            skus[p] = 0
    cost = total_price(skus)
    return cost
