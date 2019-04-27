#!/usr/bin/env python
#coding=utf-8


class Person:

    def __init__(self, name, sex, province,weight):
        print("Init the class")
        self.__name = name
        self.sex =  sex
        self.__province = province
        self._weight = weight

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_province(self, province):
        if province in ["Jilin, Hailongjiang"]:
            return "Cold "+ province
        else:
            return "Warm:"+ province


if __name__=="__main__":
    pp=Person("zhangsan","Male","Jiangsu","80")
    print(pp._weight)
    print(pp.get_name())
    pp.__name

