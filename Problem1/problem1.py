# -*- coding : utf-8 -*-

class problem1(object):
    """ maxValue以下の自然数のうちfactorsの倍数の
    和を求める
    >>> from problem1 import *
    >>> factors = [3,5]
    >>> maxValue = 1000
    >>> problem1().SumOfAllMultiples(1000,factors)
    233168
    """
    def __init__(self):
        self.__maxValue = 0
        self.__answer = 0
    def SumOfAllMultiples(self,maxValue,factors):
        self.__maxValue = maxValue
        self.__factors = factors
        if maxValue == 1:
            return 0
        for x in range(1,maxValue):
            if(x % 3 == 0) or (x % 5 == 0):
                self.__answer += x
        return self.__answer
if __name__ == "__main__":
    import doctest
    doctest.testmod()
