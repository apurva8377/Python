##################################################################################################################
#
#  Program Name : 091_CharacteristicsAll.py
#  Discription  : All variables
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

class Demo:
    No = 10

    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

print("Class variable No : ",Demo.No)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

print(f"Instance variable of obj1 : {obj1.Value1} and {obj1.Value2}")
print(f"Instance variable of obj2 : {obj2.Value1} and {obj2.Value2}")