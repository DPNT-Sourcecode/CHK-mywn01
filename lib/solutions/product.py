

class Product(object):

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def get_price(self, item_quantities):
        return item_quantities[self.name] * self.base_price

class DiscountedProduct(Product):

    def __init__(self, name, base_price, offers):
        super(DiscountedProduct, self).__init__(name, base_price)
        self.offers = offers

    def get_price(self, item_quantities):
        n = item_quantities[self.name]
        nx = []
        px = []
        for offer in self.offers[::-1]:
            ni = n // offer[0]
            nx.append(ni)
            px.append(offer[1])
            n -= ni
        return sum([nx * px for nx, px in zip(nx, px)])
