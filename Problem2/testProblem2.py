# -*- coding:utf-8 -*-
import unittest
from Fibonacci import *
from Problem2 import *

class testProblem2(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci(1,2).generate()
        self.fib_number = [1,2,3,5,8,13,21,34,55,89]
    def testFibonacci(self):
        for number in range(0,len(self.fib_number)):
            self.assertEquals(self.fib.next(),self.fib_number[number])
    def testSumOfEvenValue(self):
        self.__first = 1
        self.__second = 2 
        self.assertEqual(Problem2(self.__first,self.__second).SumOfEvenValue(10),10)
        self.assertEqual(Problem2(self.__first,self.__second).SumOfEvenValue(100),44)
if __name__ == "__main__":
    unittest.main()
