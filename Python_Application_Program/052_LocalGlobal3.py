##################################################################################################################
#
#  Program Name : 052_LocalGlobal3.py
#  Discription  : Local and Global variables
#  Author       : Apurva Vilas Shinde
#  Date         : 11/05/2026
#
##################################################################################################################

No = 11             # Global

def Fun():
    No = 21
    print("Value of No from fun is : ",No)  # 21
    No = No + 1                             # 22
    print("Value of No from Fun is : ",No)  # 22

print("Value from No is : ",No)    # 11
Fun()
print("Value of No is : ",No)      # 11