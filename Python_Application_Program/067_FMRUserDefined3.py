##################################################################################################################
#
#  Program Name : 067_FMRUserDefined3.py
#  Discription  : Filter, Map, Reduce
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

def filterX(Task , Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task,Element):
    Sum = 0

    for no in Element:
        Sum = Task(Sum,no)
    
    return Sum

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No + 1
Add = lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter is : ",FData)

    MData = list(mapX(Increment,FData))
    print("Data after map is : ",MData)

    RData = reduceX(Add,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()