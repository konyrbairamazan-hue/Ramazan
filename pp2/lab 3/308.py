class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


balance, w = map(int, input().split())

acc = Account(balance)

if acc.withdraw(w):
    print(acc.balance)
else:
    print("Insufficient Funds")