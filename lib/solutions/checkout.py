# noinspection PyUnusedLocal
# skus = unicode string
import re


class Product(object):

    def __init__(self, price, special_offer=None):
        self.price = price
        if special_offer is None:
            special_offer = (1, price)
        self.offer_amount, self.offer_price = special_offer

    def get_price(self, n):
        offer = (n // self.offer_amount) * self.offer_price
        remainder = (n % self.offer_amount) * self.price
        return offer + remainder

products = {
    'A': Product(50, (3, 130)),
    'B': Product(30, (2, 45)),
    'C': Product(20),
    'D': Product(15),
}

def parse_skus(skus):
    sku_list = re.findall(r'\d*[A-D]', skus)
    return tuple(sku_list)


def extract_skus(skus):
    sku_list = parse_skus(skus)
    if ''.join(sku_list) != skus:
        raise ValueError('Invalid SKUs supplied.')
    quantity_items = [(s[:-1], s[-1]) for s in sku_list]
    item_quantities = {}
    for q, i in quantity_items:
        if i in item_quantities:
            item_quantities[i] += int(q) if q else 1
        else:
            item_quantities[i] = int(q) if q else 1
    return item_quantities


def apply_pricing(item_quantities):
    prices = {i: products[i].get_price(q) for i, q in item_quantities.items()}
    return prices

def checkout(skus):
    try:
        skus = extract_skus(skus)
    except ValueError:
        return -1
    prices = apply_pricing(skus)
    return sum(prices.values())
