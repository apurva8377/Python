#################################################
#
#  Program Name : Data.py
#  Discription  : This program shows that variable No changes its type and memory location when reassigned.
#  Auther       : Apurva Vilas Shinde
#  Date         : 24/04/2026
#
##################################################

No = 11
print(type(No))
print(id(No))

No = 78.90
print(type(No))
print(id(No))

No = "Hello"
print(type(No))
print(id(No))