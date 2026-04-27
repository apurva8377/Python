############################################
#
#  Program Name : 39_SelectionEvenFunctionX.py
#  Discription  : Write a Python program to check even or odd using a user-defined function.
#  Auther       : Apurva Vilas Shinde
#  Date         : 27/04/2026
#
############################################

def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    CheckEven(Value)
    
if __name__ == "__main__":
    main()