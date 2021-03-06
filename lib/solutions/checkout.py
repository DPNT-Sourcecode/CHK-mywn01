# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
import itertools
from .product import products

GROUP = 'STXYZ'

def group_discount_cost(skus):
    group_items = ''
    for i in GROUP:
        group_items += i * skus.get(i, 0)
    n_group = len(group_items)
    n_extra = n_group % 3
    extra_combos = itertools.combinations(group_items, n_extra)
    extra_skus = [dict(Counter(''.join(ec))) for ec in extra_combos]
    extra_prices = [sum([products[i].get_price(es) for i in es]) for es in extra_skus]

    return (n_group // 3) * 45 + min(extra_prices)

def total_price(skus):
    cost = 0
    for p in products:
        if p in GROUP:
            continue
        product = products[p]
        cost += product.get_price(skus)
    cost += group_discount_cost(skus)
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
