############################################
#
#  Program Name : Size.py
#  Discription  : This program prints the memory size of different data types using the sys module.d prints its value and type.
#  Auther       : Apurva Vilas Shinde
#  Date         : 24/04/2026
#
############################################

import sys

No = 1198013803812093129372893723712381293723098723892739038208292720971281209641247272721890312   #int

Marks = 90.90   # float
  
Name = "Rahul"  # str

print(sys.getsizeof(No))
print(sys.getsizeof(Marks))
print(sys.getsizeof(Name))