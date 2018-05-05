# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter

VALID_PRODUCTS = ['A', 'B', 'C', 'D', 'E', 'F']


def total_price(na, nb, nc, nd, ne, nf):
    # Get numbers of collections
    na5 = na // 5
    na3 = (na % 5) // 3
    na1 = na - 5 * na5 - 3 * na3
    nb = max(0, nb - ne // 2)
    nb2 = nb // 2
    nb1 = nb % 2
    ne2 = ne // 2
    nf3 = nf // 3
    nf1 = nf % 3
    print(nf3)

    # Get costs
    ca = na5 * 200 + na3 * 130 + na1 * 50
    cb = nb2 * 45 + nb1 * 30
    cc = nc * 20
    cd = nd * 15
    ce = ne * 40
    cf = nf3 * 20 + nf1 * 10

    return ca + cb + cc + cd + ce + cf

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
