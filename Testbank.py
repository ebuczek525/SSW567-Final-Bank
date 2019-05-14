import unittest

from Bank import *

class Testbank(unittest.TestCase):

    def testWithdrawHuey_success(self):
        self.assertEqual(huey.withdraw(10), 'Right')

    def testWithdrawHuey_penalty(self):
        self.assertEqual(huey.withdraw(100), 'Right')

    def testWithdrawDewey_success(self):
        self.assertEqual(dewey.withdraw(5), 'Right')
    
    def testWithdrawDewey_penalty(self):
        self.assertEqual(dewey.withdraw(200), 'Right')
    
    def testWithdrawLouie_success(self):
        self.assertEqual(louie.withdraw(2) 'Right')
    
    def testWithdrawLouie_penalty(self):
        self.assertEqual(louie.withdraw(20), 'Right')
   
    if __name__ == '__main__':
        print('Running unit tests')
        unittest.main()
        
