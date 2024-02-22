import unittest
import prime

class TestIsPrime(unittest.TestCase):
    def test_prime(self):
        primes = [
            2, 3, 157, 163, 167, 173, 179, 181, 191,
            193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251
        ]
        for prime_num in primes:
            self.assertTrue(prime.is_prime(prime_num))

    def test_not_prime(self):
        not_primes = [
            4, 6, 8, 10, 556, 985, 294, 102398, 333,
            121, 55, 90, 555, -32, 32, 999, 18, 158, 242, 240
        ]
        for not_prime_num in not_primes:
            self.assertFalse(prime.is_prime(not_prime_num))
