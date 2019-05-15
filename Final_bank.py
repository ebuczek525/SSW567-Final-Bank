transaction = int(0)

class Bank:
    def __init__(self, name, accnum, balance):
        self.name = name
        self.accnum = accnum
        self.balance = balance
    def withdraw(self, amount):
        global transaction
        if amount <= (0.1 * self.balance):
            if self.name == 'Huey':
                self.balance -= amount
                dewey.balance += amount
                louie.balance += amount
                scrooge.balance -= (2 * amount)
                transaction += 1
            elif self.name == 'Dewey':
                self.balance -= amount
                huey.balance += amount
                louie.balance += amount
                scrooge.balance -= (2 * amount)
                transaction += 1
            elif self.name == 'Louie':
                self.balance -= amount
                dewey.balance += amount
                huey.balance += amount
                scrooge.balance -= (2 * amount)
                transaction += 1
        elif amount > (0.1 * self.balance):
            self.balance -= 5
            scrooge.balance += 5
            transaction += 1
            
        print("Transaction number",transaction)
        print("Huey's balance is",huey.balance)
        print("Dewey's balance is",dewey.balance)
        print("Louie's balance is",louie.balance)
        print("Scrooge McDuck's balance is",scrooge.balance)

huey = Bank('Huey', '700007', 150)
dewey = Bank('Dewey', '800008', 350)
louie = Bank('Louie', '900009', 25)
scrooge = Bank('Scrooge McDuck', '100001', 1000000)
