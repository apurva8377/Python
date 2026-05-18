##################################################################################################################
#
#  Program Name : 095_Encapsulation.py
#  Discription  : All variables
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object gets created succsesfully")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans 
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithmatic(11,21)     # Arithematic(id(obj1),11,10)  -> __init__(id(obj1),11,10)
obj2 = Arithmatic(21,20)     # Arithematic(id(obj2),21,20)  -> __init__(id(obj2),21,20)

Ret = obj1.Addition()       # Addition(id(obj1)) -> Addition(1000)
print(Ret)  # 32

Ret = obj2.Substraction()   # Substraction(id(obj2))    -> Substraction(2000)
print(Ret)  # 1
