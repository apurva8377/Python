##################################################################################################################
#
#  Program Name : 115_Schedular4.py
#  Discription  : Automation program
#  Author       : Apurva Vilas Shinde
#  Date         : 14/06/2026
#
##################################################################################################################

import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def gun():
    print("Inside gun at : ",datetime.datetime.now())

def main():
    print("Inside marvellous Automation Script at : ",datetime.datetime.now())

    #schedule.every(20).seconds.do(fun)

    schedule.every(1).minute.do(fun)

    schedule.every(1).hour.do(gun)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()