##################################################################################################################
#
#  Program Name : 100_Inheritance.py
#  Discription  : Inheritance
#  Author       : Apurva Vilas Shinde
#  Date         : 18/05/2026
#
##################################################################################################################

class Parent:
    def __init__(self):
        print("Inside parent constructor")
        self.No1 = 10
        self.No2 = 20

    def fun():
        print("Inside fun method of parent")

class child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")
        self.A = 11
        self.B = 21

    def sun():
        print("Inside sun method of chile")

cobj = child()