##################################################################################################################
#
#  Program Name : 113_Schedular2.py
#  Discription  : Automation program
#  Author       : Apurva Vilas Shinde
#  Date         : 13/06/2026
#
##################################################################################################################

import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation script at : ",datetime.datetime.now())

    schedule.every(20).seconds.do(fun)

    # Problem

if __name__ == "__main__":
    main()