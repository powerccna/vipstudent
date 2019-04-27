#! /usr/bin/env python
#coding=utf-8


class Person:

    def __init__(self):
        self.sex = ''

    def sex(self):
        pass

    def weight(self):
        pass

    def age(self):
        pass

    def set_sex(self,sex):
        self.sex=sex


if __name__=='__main__':
    toni_instance = Person()
    toni_instance.set_sex('男')
    print(toni_instance.sex)

