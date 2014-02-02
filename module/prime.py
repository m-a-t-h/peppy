# -*- coding: utf-8 -*-

class Prime:
    def __generate_prime(self,):
        """
        >>> P = Prime()
        >>> P.__generate_prime()
        Traceback (most recent call last):
        AttributeError: Prime instance has no attribute '__generate_prime'
        """
        primes = [2]
        p_candidate = 1
        while True:
            p_candidate += 2
            is_prime = True
            # p_candidate を素数で割っていく
            for p in primes:
                if p_candidate < p * p:
                    break
                if p_candidate % p == 0:
                    is_prime = False
                    break
            if is_prime:
                yield primes[-1]
                primes.append(p_candidate)

    """
    素数を n 個小さい順に取得する
    """
    def get_n_primes(self, n):
        """
        >>> P = Prime()
        >>> P.get_n_primes(1)
        [2]

        >>> P.get_n_primes(25)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        >>> P.get_n_primes(-1)
        Traceback (most recent call last):
        ValueError: input has to be a positive int or long: -1
        """
        if isinstance(n, (int, long)) == False or n <= 0:
            raise ValueError("input has to be a positive int or long: %s" %n)
        ret = []
        prime = self.__generate_prime()
        for i in range(n):
            next = prime.next()
            ret.append(next)
        return ret

    def get_primes_by_upper_limit(self, upper_limit):
        """
        >>> P = Prime()
        >>> P.get_primes_by_upper_limit(2)
        [2]

        >>> P.get_primes_by_upper_limit(100)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        >>> P.get_primes_by_upper_limit(-1)
        Traceback (most recent call last):
        ValueError: input has to be a number (>= 2): -1
        """
        import numbers
        if isinstance(upper_limit, numbers.Number) == False or upper_limit < 2:
            raise ValueError("input has to be a number (>= 2): %s" %upper_limit)
        ret = []
        prime = self.__generate_prime()
        next = prime.next()
        while next <= upper_limit:
            ret.append(next)
            next = prime.next()
        return ret

    # 与えられた数を素因数分解し、連想配列の形で返す
    # 2 以上の整数 a, b (a != b) と、素数 p, q (p != q) があるとして
    # n = (a ** p) * (b ** q) のとき、get_prime_factors(n) = {a: p, b: q}
    def get_prime_factors(self, n):
        """
        >>> P = Prime()
        >>> P.get_prime_factors(2)
        {2: 1}

        >>> P.get_prime_factors(100)
        {2: 2, 5: 2}

        >>> P.get_prime_factors(-1)
        Traceback (most recent call last):
        ValueError: input has to be a positive int or long (>= 2): -1
        """
        if isinstance(n, (int, long)) == False or n <= 1:
            raise ValueError("input has to be a positive int or long (>= 2): %s" %str(n))
        ret = {}
        import math
        # use math.sqrt for speedup
        if n >= 4:
            n_sqrt = math.sqrt(n)
        else:
            n_sqrt = 2
        primes = self.get_primes_by_upper_limit(n_sqrt)

        # divide by primes
        n_orig = n
        for p in primes:
            if n == 1:
                break
            while n % p == 0:
                n /= p
                if p in ret:
                    ret[p] += 1
                else:
                    ret[p]  = 1
        # add n to ret
        if n == n_orig:
            # in this case, n_orig is prime
            ret[n_orig] = 1
        elif n != 1:
            # this happens when n is prime and is not included in primes
            ret[n] = 1
        return ret

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed:
        import sys
        sys.exit(1)
