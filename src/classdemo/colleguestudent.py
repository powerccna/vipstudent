#! /usr/bin/env python
#coding=utf-8


from classdemo.student import Student

class CollStudent(Student):

    def __init__(self,name, sex, province ):
        Student.__init__(self,name, sex, province)

    def has_peer(self):
        return self.peer

    def set_peer(self,peer=None):
        if peer:
            self.peer= True
        else:
            self.peer = False

if __name__=='__main__':
    toni_instance = Student('toni','男','湖南')
    print(toni_instance.get_name())


