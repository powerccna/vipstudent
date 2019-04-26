#!/usr/bin/env python
#coding=utf-8


class Person:

    def set_name(self,name):
        self.name= name

    def get_name(self):
        return self.name

    def set_person_attribute(self, sex, province):
        self.sex = sex
        self.province = province

    def get_sex(self):
        return self.sex



if __name__=="__main__":
    per1  = Person()
    per1.set_name("hanmeimei")
    print(per1.get_name())
    per1.set_person_attribute("Female","Shanghai")
    print(per1.get_sex())
