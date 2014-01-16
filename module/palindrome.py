# -*- coding: utf-8 -*-

class Palindrome:
    def __is_palindrome(self, integer):
        """
        >>> P = Palindrome()
        >>> P.__is_palindrome()
        Traceback (most recent call last):
        AttributeError: Palindrome instance has no attribute '__is_palindrome'
        """
        return str(integer) == str(integer)[::-1]

    # 与えられた桁数の 2 つの数の積のうち、最大の回文数を求める
    def get_largest_palindrome_product_of_two_numbers_by_keta(self, keta):
        """
        >>> P = Palindrome()
        >>> P.get_largest_palindrome_product_of_two_numbers_by_keta(2)
        9009

        >>> P.get_largest_palindrome_product_of_two_numbers_by_keta(-1)
        Traceback (most recent call last):
        ValueError: input has to be a positive int or long: -1
        """
        if isinstance(keta, (int, long)) == False or keta <= 0:
            raise ValueError("input has to be a positive int or long: %s" %keta)
        max = 0
        low  = pow(10, keta - 1)
        high = pow(10, keta) - 1
        for first in range(high, low-1, -1): # [high, high-1, high-2, ... low]
            if first * high < max:
                break
            for second in range(high, low-1, -1):
                tmp_max = first * second
                if self.__is_palindrome(tmp_max) and max < tmp_max:
                    max = tmp_max
                    break
        return max

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed:
        import sys
        sys.exit(1)

