##################################################################################################################
#
#  Program Name : 130_FileIOPath.py
#  Discription  : File handeling in python
#  Author       : Apurva Vilas Shinde
#  Date         : 16/06/2026
#
##################################################################################################################

import os

def main():
    FileName = input("Enter the name of file : ")

    Ret = os.path.isabs(FileName)

    if(Ret == True):
        print("It is absolute path")
    else:
        print("It is relative path")

if __name__ == "__main__":
    main()