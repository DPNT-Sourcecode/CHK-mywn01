import re

# noinspection PyUnusedLocal
# skus = unicode string
def extract_skus(skus):
    sku_list = re.findall(r'\d*[A-D]', skus)
    return tuple(sku_list)


def checkout(skus):
    raise NotImplementedError()
