#!/usr/bin/env python
#coding=utf-8


class Person:

    def __init__(self, name, sex, province,weather):
        print("Init the class")
        self.__name = name
        self.sex =  sex
        self.__province = province
        self._weather = weather

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
    pp=Person("zhangsan","Male","Jiangsu","Warm")
    print (pp.sex)
    #print(pp.__province)
    print (pp._weather)
    #print pp.__name
    print (pp.get_name())

    #print pp._Person__name