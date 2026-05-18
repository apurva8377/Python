##################################################################################################################
#
#  Program Name : 056_ListDynamicInput1.py
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

    print(Data)

if __name__ == "__main__":
    main()