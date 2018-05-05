import re

# noinspection PyUnusedLocal
# skus = unicode string
def extract_skus(skus):
    sku_list = re.findall(r'\d*[A-D]', skus)
    if sum(sku_list) != skus:
        raise ValueError('Invalid SKUs')
    quantity_items = [(s[:-1], s[-1]) for s in sku_list]
    item_quantities = {q[1]: q[0] for q in quantity_items}
    return item_quantities


def checkout(skus):
    try:
        skus = extract_skus(skus)
    except ValueError:
        return -1
