##################################################################################################################
#
#  Program Name : 050_LocalGlobal1.py
#  Discription  : Local and Global variables
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

No = 11             # Global

def Fun():
    No = 21         # Local
    print("Value of No from fun is : ",No)  # 21

print("Value from No is : ",No)    # 11
Fun()