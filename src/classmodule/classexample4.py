#!/usr/bin/env python
#coding=utf-8


from classmodule.classexample2 import Person

class Student(Person):

    def __init__(self,name, sex, province, grade):
        #super(Student, self).__init__(name, sex, province)
        Person.__init__(self,name, sex, province)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "我不告诉你student名字"

    def get_nick_name(self):
        name  = Person.get_name(self)
        if name.startswith("xiao"):
            return name.replace("xiao","small_")
        else:
            return name

if __name__=="__main__":
    ss=Student("xiaozhang","Male","Beijing",6)
    print(ss.get_nick_name())

