#!/usr/bin/env python
#coding=utf-8


from classmodule.classexample4 import Student
from classmodule.classexample2 import Person

class SeniorStudent(Student):

    def __init__(self,name, sex, province, grade):
        #super(StudentSenior, self).__init__(name, sex, province,grade)
        Student.__init__(self,name, sex, province,grade)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "我不告诉你Girl名字"

    def overtime_study(self):
        if self.grade == 3:
            return u"补课"
        else:
            return u"不补课"

    def get_new_name(self):
        name  = Person.get_name(self)
        if name.startswith("xiao"):
            print("small")
        else:
            print("big")


if __name__=="__main__":
    sg=SeniorStudent("huahua","Female","Shanghai",3)
    print(sg.get_name())
    sg.get_new_name()
    #print(sg.get_sex())
