

class Product(object):

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def get_price(self, item_quantities):
        return item_quantities[self.name] * self.base_price

class DiscountedProduct(Product):

    def __init__(self, name, base_price, offers = ()):
        super(DiscountedProduct, self).__init__(name, base_price)
        self.offers = offers

    def get_price(self, item_quantities):
        n = item_quantities.get(self.name, 0)
        nx = []
        px = []
        for offer in self.offers[::-1]:
            ni = n // offer[0]
            nx.append(ni)
            px.append(offer[1])
            n -= ni * offer[0]
        nx.append(n)
        px.append(self.base_price)
        return sum([nx * px for nx, px in zip(nx, px)])

class BProduct(Product):

    def get_price(self, item_quantities):
        nb = item_quantities.get('B', 0)
        ne = item_quantities.get('E', 0)
        nb = max(0, nb - ne // 2)
        nb2 = nb // 2
        nb1 = nb % 2
        return nb2 * 45 + nb1 * self.base_price

class MProduct(Product):

    def get_price(self, item_quantities):
        nm = item_quantities.get('M', 0)
        nn = item_quantities.get('N', 0)
        nm = max(0, nm - nn // 3)
        return nm * self.base_price

class QProduct(Product):

    def get_price(self, item_quantities):
        nq = item_quantities.get('Q', 0)
        nr = item_quantities.get('R', 0)
        nq = max(0, nq - nr // 3)
        nq3 = nq // 3
        nq1 = nq % 3
        print(nq)
        return nq3 * 80 + nq1 * self.base_price



A = DiscountedProduct('A', 50, ((3, 130), (5, 200)))
B = BProduct('B', 30)
C = Product('C', 20)
D = Product('D', 15)
E = Product('E', 40)
F = DiscountedProduct('F', 10, offers = ((3, 20),))
G = Product('G', 20)
H = DiscountedProduct('H', 10, offers=((5, 45), (10, 80)))
I = Product('I', 35)
J = Product('J', 60)
K = DiscountedProduct('K', 70, offers=((2, 120),))
L = Product('L', 90)
M = MProduct('M', 15)
N = Product('N', 40)
O = Product('O', 10)
P = DiscountedProduct('P', 50, ((5, 200),))
Q = QProduct('Q', 30)
R = Product('R', 50)
S = Product('S', 20)
T = Product('T', 20)
U = DiscountedProduct('U', 40, ((4, 120),))
V = DiscountedProduct('V', 50, ((2, 90), (3, 130)))
W = Product('W', 20)
X = Product('X', 17)
Y = Product('Y', 20)
Z = Product('Z', 21)

products = {
    'A': A,
    'B': B,
    'C': C,
    'D': D,
    'E': E,
    'F': F,
    'G': G,
    'H': H,
    'I': I,
    'J': J,
    'K': K,
    'L': L,
    'M': M,
    'N': N,
    'O': O,
    'P': P,
    'Q': Q,
    'R': R,
    'S': S,
    'T': T,
    'U': U,
    'V': V,
    'W': W,
    'X': X,
    'Y': Y,
    'Z': Z,
}
