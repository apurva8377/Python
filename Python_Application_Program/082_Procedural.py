##################################################################################################################
#
#  Program Name : 082_Procedural.py
#  Discription  : Procedural program
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

def Addition(A,B):
    return A+B

def Substraction(A,B):
    return A-B

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Ans = Addition(No1,No2)
print("Addition is : ",Ans)

Ans = Substraction(No1,No2)
print("Substraction is : ",Ans) 