##################################################################################################################
#
#  Program Name : 053_LocalGlobal4.py
#  Discription  : Local and Global variables
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

No = 11             # Global

def Fun():
    global No
    print("Value of No from fun is : ",No)  # 11
    No = No + 1                             # 12
    print("Value of No from Fun is : ",No)  # 12

print("Value from No is : ",No)    # 11
Fun()
print("Value of No is : ",No)      # 12