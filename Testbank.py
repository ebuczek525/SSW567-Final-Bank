import unittest

from 567_bank import *

class Testbank(unittest.TestCase):

    def testWithdrawHuey_success(self):
        self.assertEqual(withdraw(Huey, 10), 'Right')

    def testWithdrawHuey_penalty(self):
        self.assertEqual(withdraw(Huey, 100), 'Right')

    def testWithdrawDewey_success(self):
        self.assertEqual(withdraw(Dewey, 5), 'Right')
    
    def testWithdrawDewey_penalty(self):
        self.assertEqual(withdraw(Dewey, 200), 'Right')
    
    def testWithdrawLouie_success(self):
        self.assertEqual(withdraw(Louie, 2) 'Right')
    
    def testWithdrawLouie_penalty(self):
        self.assertEqual(withdraw(Louie, 20), 'Right')
    

    if __name__ == '__main__':
        print('Running unit tests')
        unittest.main()
