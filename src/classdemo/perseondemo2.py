#! /usr/bin/env python
#coding=utf-8

class Person:

    total_person = 0

    def __init__(self, name, sex, province):
        #print("Init the class")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_location(self):
        return self.province

    def set_weigth(self, weight):
        self.weight = weight

    def get_weigth(self):
        return  self.weight


if __name__=='__main__':
    toni_instance=Person('toni','男','湖南')
    print(toni_instance.total_person)
    print(toni_instance.sex)
    print('*'*10)
    wutong_instance = Person('梧桐','女','广东')
    print(toni_instance.total_person)
    print(toni_instance.total_person)
    print(toni_instance.get_name())
    print('*' * 10)
    print(wutong_instance.total_person)

