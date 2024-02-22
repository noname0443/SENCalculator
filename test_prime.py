import prime
import unittest

class Test_TestIsPrime(unittest.TestCase):
    def test_prime(self):
        primes = [2, 3, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
        for primeNum in primes:
            self.assertTrue(prime.IsPrime(primeNum))

    def test_not_prime(self):
        notPrimes = [4, 6, 8, 10, 556, 985, 294, 102398, 333, 121, 55, 90, 555, -32, 32, 999, 18, 158, 242, 240]
        for notPrime in notPrimes:
            self.assertFalse(prime.IsPrime(notPrime))
