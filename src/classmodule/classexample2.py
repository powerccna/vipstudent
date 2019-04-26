#!/usr/bin/env python
#coding=utf-8

class Person(object):

    total_person=0
    def __init__(self, name, sex, province):
        print("Init the class")
        self.name = name
        self.sex =  sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex


if __name__=="__main__":
    person1 = Person("xiaozhang","Male","Beijing")
    #person1 = Person()
    print(person1.sex)
    print(person1.name)
    print(person1.get_name())
    print(person1.total_person)
    print("*"*50)

    person2 = Person("Hanmeimei", "Female", "Shanghai")
    print(person2.sex)
    print(person2.total_person)
