import unittest

from Final_bank import *

class Testbank(unittest.TestCase):

    def test1WithdrawHuey_success(self):
        huey.withdraw(10)
        self.assertEqual(huey.balance, 140)
        self.assertEqual(dewey.balance, 360)
        self.assertEqual(louie.balance, 35)
        self.assertEqual(scrooge.balance, 999980)
        self.assertEqual(transaction, 1)
        
    def test2WithdrawHuey_penalty(self):   
        huey.withdraw(100)
        self.assertEqual(huey.balance, 135)
        self.assertEqual(dewey.balance, 360)
        self.assertEqual(louie.balance, 35)
        self.assertEqual(scrooge.balance, 999985)
        self.assertEqual(transaction, 2)
        
    def test3WithdrawDewey_success(self):
        dewey.withdraw(5)
        self.assertEqual(huey.balance, 140)
        self.assertEqual(dewey.balance, 355)
        self.assertEqual(louie.balance, 40)
        self.assertEqual(scrooge.balance, 999975)
        self.assertEqual(transaction, 3)
        
    def test4WithdrawDewey_penalty(self):
        dewey.withdraw(200)
        self.assertEqual(huey.balance, 140)
        self.assertEqual(dewey.balance, 350)
        self.assertEqual(louie.balance, 40)
        self.assertEqual(scrooge.balance, 999980)
        self.assertEqual(transaction, 4)
    
    def test5WithdrawLouie_success(self):
        louie.withdraw(2)
        self.assertEqual(huey.balance, 142)
        self.assertEqual(dewey.balance, 352)
        self.assertEqual(louie.balance, 38)
        self.assertEqual(scrooge.balance, 999976)
        self.assertEqual(transaction, 5)
       
    def test6WithdrawLouie_penalty(self):
        louie.withdraw(20)
        self.assertEqual(huey.balance, 142)
        self.assertEqual(dewey.balance, 352)
        self.assertEqual(louie.balance, 33)
        self.assertEqual(scrooge.balance, 999981)
        self.assertEqual(transaction, 6)
    
    if __name__ == '__main__':
        print('Running unit tests')
        unittest.main()
       
