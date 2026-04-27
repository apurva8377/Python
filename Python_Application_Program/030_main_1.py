############################################
#
#  Program Name : 30_main_1.py
#  Discription  : Write a Python program to define a user-defined function for multiplication of two numbers.
#  Auther       : Apurva Vilas Shinde
#  Date         : 27/04/2026
#
############################################

def Multiplication(Value1, Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = Multiplication(No1,No2)
    print("Multiplication is : ",Result)

main()