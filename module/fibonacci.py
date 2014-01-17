# -*- coding: utf-8 -*-

class Fibonacci:
    def __generate_fib(self,):
        """
        >>> F = Fibonacci()
        >>> F.__generate_fib()
        Traceback (most recent call last):
        AttributeError: Fibonacci instance has no attribute '__generate_fib'
        """
        fib = [1,2]
        next = 3
        while True:
            fib.append(next)
            yield fib[-1]
            next += fib[-2]

    def get_fibs_by_upper_limit(self, upper_limit):
        """
        >>> F = Fibonacci()
        >>> F.get_fibs_by_upper_limit(2)
        [1, 2]

        >>> F.get_fibs_by_upper_limit(100)
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        >>> F.get_fibs_by_upper_limit(-1)
        Traceback (most recent call last):
        ValueError: input has to be a number (>= 2): -1
        """
        import numbers
        if isinstance(upper_limit, numbers.Number) == False or upper_limit < 2:
            raise ValueError("input has to be a number (>= 2): %s" %upper_limit)
        ret = [1, 2]
        fib = self.__generate_fib()
        next = fib.next()
        while next <= upper_limit:
            ret.append(next)
            next = fib.next()
        return ret

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed:
        import sys
        sys.exit(1)

