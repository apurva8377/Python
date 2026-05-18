##################################################################################################################
#
#  Program Name : 102_InheritanceXX.py
#  Discription  : Inheritance
#  Author       : Apurva Vilas Shinde
#  Date         : 18/05/2026
#
##################################################################################################################

class Parent:
    def __init__(self):
        print("Inside Parent constructor")

    def fun(self):
        print("Inside fun method of Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")

    def fun(self):
        super().fun()
        print("Inside fun method of Child")

cobj = Child()

cobj.fun()