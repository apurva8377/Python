############################################
#
#  Program Name : 38_SelectionEvenFunction.py
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
    CheckEven(21)        # Positional Argument = Value is passed based on position.
    CheckEven(No = 22)   # Keyword Argument = Value is passed using parameter name.

if __name__ == "__main__":
    main()