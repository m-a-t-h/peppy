# -*- coding: utf-8 -*-

import sys,os
import time

class Performance:
    def __init__(self,):
        return

    """
    returns true if func1 is faster than func2
    """
    def compare_functions(self, obj1, func1, params1,
                          obj2, func2, params2, iteration=10000):
        """
        >>> P = Performance()
        >>> P.compare_functions(sys.modules['time'], 'sleep', [1,], sys.modules['time'], 'sleep', [5,], iteration = 1)
        True
        """
        start_time1 = time.time()
        for i in xrange(iteration):
            method1 = getattr(obj1, func1)
            method1(*params1) # if params1 = (1,2), method1(*params1) means method1(1,2)
        end_time1 = time.time()

        start_time2 = time.time()
        for i in xrange(iteration):
            method2 = getattr(obj2, func2)
            method2(*params2)
        end_time2 = time.time()

        return (end_time1 - start_time1) <= (end_time2 - start_time2)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed:
        import sys
        sys.exit(1)
