import re

# noinspection PyUnusedLocal
# skus = unicode string
def extract_skus(skus):
    sku_list = re.findall(r'\d*[A-D]', skus)
    if ''.join(sku_list) != skus:
        raise ValueError('Invalid SKUs supplied.')
    quantity_items = [(s[:-1], s[-1]) for s in sku_list]
    item_quantities = {}
    for q, i in quantity_items:
        if i in item_quantities:
            item_quantities[i] += int(q)
        else:
            item_quantities[i] = int(q) if q else 1
    return item_quantities


def checkout(skus):
    try:
        skus = extract_skus(skus)
    except ValueError:
        return -1
