# -*- coding:utf-8 -*-

class Fibonacci(object):
    def __init__(self,first,second):
        self.__first = first
        self.__second = second
    def generate(self):
        while True:
            yield self.__first
            self.__first,self.__second = self.__second,self.__first + self.__second
