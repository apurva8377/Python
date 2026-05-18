##################################################################################################################
#
#  Program Name : 057_ListDynamicInput2.py
#  Discription  : Dynamic input into the list
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Sum = 0

    for i in range(Size):
        Sum = Sum + Data[i]

    print("The Summation is : ",Sum)
    
if __name__ == "__main__":
    main()