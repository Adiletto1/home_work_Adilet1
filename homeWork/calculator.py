class Calculator:
    def __init__(self, one):
        self.one = one

    def __add__(self, other):
        return other + self.one

    def __sub__(self, other):
        return other - self.one

    def __mul__(self, other):
        return other * self.one

    def __truediv__(self, other):
        return other / self.one

a = Calculator(5)
b = Calculator(5)
c = a + b
print(c)


