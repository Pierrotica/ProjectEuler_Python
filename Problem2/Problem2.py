# -*- coding:utf-8 -*-
from Fibonacci import *

class Problem2(object):
    def __init__(self,first,second):
        self.__first = first
        self.__second = second
        self.__answer = 0
    def SumOfEvenValue(self,maxValue):
        self.__maxValue = maxValue
        self.__fib = Fibonacci(self.__first,self.__second).generate()
        while True:
            self.__fib_Value = self.__fib.next()
            if(self.__fib_Value <= self.__maxValue):
                if((self.__fib_Value % 2) == 0):
                    self.__answer += self.__fib_Value
            else:
                break
        return self.__answer
if __name__ == "__main__":
    answer = Problem2(1,2).SumOfEvenValue(4000000)
    print answer
