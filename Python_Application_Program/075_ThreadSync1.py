##################################################################################################################
#
#  Program Name : 075_ThreadSync1.py
#  Discription  : MultiThreading
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

import threading

iCnt = 0

def Update():
    global iCnt

    for _ in range(2000000):
        iCnt = iCnt + 1

def main():
    global iCnt

    Update()
    Update()

    print("Value of iCnt is : ",iCnt)

if __name__ == "__main__":
    main()