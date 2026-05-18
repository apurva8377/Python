##################################################################################################################
#
#  Program Name : 089_CharacteristicsClassX.py
#  Discription  : Class Variables
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

import gc

class Demo:
    No1 = 10
    No2 = 11

    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside Destructor")

print(Demo.No1)
print(Demo.No2)