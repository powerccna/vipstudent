#! /usr/bin/env python
#coding=utf-8

from classdemo.perseondemo2 import Person

class Student(Person):

    def __init__(self,name, sex, province ):
        Person.__init__(self,name, sex, province)

    def set_grade(self,grade):
        self.grade =grade

    def get_sex(self):
        return '我不告诉你'


if __name__=='__main__':
    toni_instance = Student('toni','男','湖南')
    print(toni_instance.get_name())
    print(toni_instance.get_sex())