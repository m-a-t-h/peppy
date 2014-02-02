# -*- coding: utf-8 -*-

import sys,os
sys.path.append( os.path.abspath(os.path.dirname(__file__)) )
from prime import Prime
from permutation import Permutation
from util.performance import Performance

class Divisor:
    def __init__(self,):
        self.__mod_prime = Prime()
        self.__mod_permutation = Permutation()

    def get_count_of_divisors(self, n):
        """
        >>> D = Divisor()
        >>> D.get_count_of_divisors(2)
        2

        >>> D.get_count_of_divisors(100)
        9

        >>> D.get_count_of_divisors(-1)
        Traceback (most recent call last):
        ValueError: input has to be a positive int or long: -1
        """
        if isinstance(n, (int, long)) == False or n <= 0:
            raise ValueError("input has to be a positive int or long: %s" %n)
        if n == 1:
            return 1
        # n = (a ** p) * (b ** q) * (c ** r) のとき、
        # n の約数は (p + 1) * (q + 1) * (r + 1) で求められる
        factors = self.__mod_prime.get_prime_factors(n)
        powers = [v + 1 for v in factors.values()] # [p+1, q+1, r+1, ...]
        return reduce(lambda x, y: x * y, powers)

    # TODO: optimize performance by changing n_large
    def get_proper_divisors(self, n, n_large = 10000):
        """
        >>> D = Divisor()
        >>> D.get_proper_divisors(28)
        [1, 2, 4, 7, 14]

        >>> D.get_proper_divisors(200)
        [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100]
        """
        if n >= n_large:
            return self._get_pds1(n)
        else:
            return self._get_pds2(n)

    def _get_pds1(self, n):
        prime_factors = self.__mod_prime.get_prime_factors(n)

        # prime_all_powers
        prime_all_powers = {}
        # for n=600 primes = [2, 3, 5]
        for prime,power in prime_factors.items(): # for n=200 prime=2,5
            prime_all_powers[prime] = [prime * pw for pw in range(power)]
        # for n=600 prime_all_powers = {2:[1,2,4,8], 3:[1,3], 5:[1,5,25]}

        res = []
        for pair in self.__mod_permutation.get_all_permutations(prime_all_powers.values()):
            # pairs: [1,1,1], [1,1,5], [1,1,25], [1,3,1], [1,3,5], [1,3,25], .... [8,3,25]
            res.append( reduce(lambda x,y: int(x)*int(y), pair) )
        return res

    def _get_pds2(self, n):
        pds = []
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                pds.append( i )
        return pds

    def test_pds_performance(self, n):
        """
        >>> D = Divisor()
        >>> D.test_pds_performance(100)
        False
        >>> D.test_pds_performance(300)
        False
        >>> D.test_pds_performance(1000)
        False
        >>> D.test_pds_performance(2000)
        False
        >>> D.test_pds_performance(2500)
        True
        >>> D.test_pds_performance(3000)
        True
        >>> D.test_pds_performance(10000)
        True
        """
        P = Performance()
        return P.compare_functions(self, '_get_pds1', [n,],
                                   self, '_get_pds2', [n,])


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed:
        import sys
        sys.exit(1)
