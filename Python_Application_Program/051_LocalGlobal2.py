##################################################################################################################
#
#  Program Name : 051_LocalGlobal2.py
#  Discription  : Local and Global variables
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

No = 11             # Global

def Fun():
    print("Value of No from fun is : ",No)  # 11

print("Value from No is : ",No)    # 11
Fun()