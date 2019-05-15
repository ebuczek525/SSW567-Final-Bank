class Bank:
    def __init__(self, name, accnum, balance):
        self.name = name
        self.accnum = accnum
        self.balance = balance
    def withdraw(self, amount):
        if amount <= (0.1 * self.balance):
            if self.name == 'Huey':
                self.balance -= amount
                dewey.balance += amount
                louie.balance += amount
                scrooge.balance -= (2 * amount)
            elif self.name == 'Dewey':
                self.balance -= amount
                huey.balance += amount
                louie.balance += amount
                scrooge.balance -= (2 * amount)
            elif self.name == 'Louie':
                self.balance -= amount
                dewey.balance += amount
                huey.balance += amount
                scrooge.balance -= (2 * amount)
        elif amount > (0.1 * self.balance):
            self.balance -= 5
            scrooge.balance += 5

huey = Bank('Huey', '700007', 150)
dewey = Bank('Dewey', '800008', 350)
louie = Bank('Louie', '900009', 25)
scrooge = Bank('Scrooge McDuck', '100001', 1000000)
