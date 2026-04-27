############################################
#
#  Program Name : BinaryXX.py
#  Discription  : This program demonstrates bytes as an ordered, immutable data type and prints its values and element.
#  Auther       : Apurva Vilas Shinde
#  Date         : 24/04/2026
#
############################################

# Indexed
# Ordered
# Immutable

Data = bytearray([65,97,98])

print(Data)
print(type(Data))
print(Data[0])

Data[0] = 66  
print(Data[0])