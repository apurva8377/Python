##################################################################################################################
#
#  Program Name : 054_List1.py
#  Discription  : List
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("The elements are :   ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Summation(Data)

    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()