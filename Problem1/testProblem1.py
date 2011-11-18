# -*- coding : utf-8 -*-
import unittest
from problem1 import *


class testSumOfMultiples(unittest.TestCase):
    def setUp(self):
        self.factors = [3,5]
        self.answerPair = ((1,0),(2,0),(3,0),(4,3),(5,3),(6,8),(7,14),(8,14),(9,14),(10,23),(16,60))
    def test_maxValue(self):
        for x in range(0,len(self.answerPair)):
            print "最大値が%dの時の期待値：%d"%(x + 1,self.answerPair[x][1])
            self.assertEqual(problem1().SumOfAllMultiples(self.answerPair[x][0],self.factors),self.answerPair[x][1])

if __name__ == "__main__":
    unittest.main()
