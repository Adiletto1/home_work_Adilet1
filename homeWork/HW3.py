class Bank:
    def __init__(self, _name, _balance):
        self.name = _name
        self.balance = _balance

    def moneyX(self):
        cash = int(input('На сколько хотите пополнить баланс? :'))
        return print(self.balance + cash)

    def _kill(self):
        self.balance = 0
        return self.balance

    def __jackpot(self):
        return self.balance * 100

    def moneyPlus(self, you):
        self.balance += you.balance


b = Bank('adi', 100)
r = Bank('beka', 100)
r.moneyPlus(b)
print(r.balance)

