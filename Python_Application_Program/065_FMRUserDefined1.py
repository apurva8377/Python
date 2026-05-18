##################################################################################################################
#
#  Program Name : 065_FMRUserDefined1.py
#  Discription  : Filter, Map, Reduce
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

from functools import reduce

def filterX(Task , Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No + 1
Add = lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after map is : ",MData)

    RData = reduce(Add,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()