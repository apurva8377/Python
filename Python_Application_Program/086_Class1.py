##################################################################################################################
#
#  Program Name : 086_Class1.py
#  Discription  : Constructor ,Destructor
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")

obj = Demo()

print("End of application")