############################################
#
#  Program Name : 29_UserFunction_2.py
#  Discription  : Write a Python program to define a user-defined function for multiplication of two numbers.
#  Auther       : Apurva Vilas Shinde
#  Date         : 27/04/2026
#
############################################

def Multiplication(Value1,Value2):
    Ans = 0     # Local variable
    Ans = Value1 * Value2
    return Ans

print("Demo Application")

No1 = 10
No2 = 11

Result = 0

Result = Multiplication(No1,No2)
print("Multiplication is : ",Result)