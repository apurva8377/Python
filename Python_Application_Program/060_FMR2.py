##################################################################################################################
#
#  Program Name : 060_FMR2.py
#  Discription  : Filter, Map, Reduce
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+1

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after map is : ",MData)

if __name__ == "__main__":
    main()