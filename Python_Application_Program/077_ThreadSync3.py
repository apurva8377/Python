##################################################################################################################
#
#  Program Name : 077_ThreadSync3.py
#  Discription  : MultiThreading
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

import threading

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt

    for _ in range(2000000):
        with lobj:
            iCnt = iCnt + 1

def main():
    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt is : ",iCnt)

if __name__ == "__main__":
    main()
