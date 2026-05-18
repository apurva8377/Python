##################################################################################################################
#
#  Program Name : 044_FunctionIndustrialXX.py
#  Discription  : Write a Python program to check even or odd using a user-defined function.
#  Auther       : Apurva Vilas Shinde
#  Date         : 27/04/2026
#
##################################################################################################################

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEven(Value)

    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")

if __name__ == "__main__":
    main()
