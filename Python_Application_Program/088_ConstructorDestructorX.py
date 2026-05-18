##################################################################################################################
#
#  Program Name : 088_ConstructorDestructorX.py
#  Discription  : Constructor ,Destructor
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

import gc

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate
obj1 = Demo()
obj2 = Demo()

# Use

# Deallocate
del obj1
del obj2

gc.collect()

print("End of application")
