#!/usr/bin/env python
#coding=utf-8

class Person:

    def __init__(self):
        print("Init the class")
        self.age =''
        self.province ='北京'
        self.name=''


    def set_profile(self,age, province,name):
        self.age = age
        self.province= province
        self.name = name

    def get_profile(self,name):
        return self.age,self.province



if __name__=="__main__":
    chaoren = Person()
    chaoren.set_profile(18,'湖北','超人会飞')
    print(chaoren.get_profile('超人会飞'))


