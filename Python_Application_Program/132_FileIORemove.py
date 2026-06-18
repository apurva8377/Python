##################################################################################################################
#
#  Program Name : 132_FileIORemove.py
#  Discription  : File handeling in python
#  Author       : Apurva Vilas Shinde
#  Date         : 16/06/2026
#
##################################################################################################################

import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("The file gets deleted")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()