##################################################################################################################
#
#  Program Name : 134_FileIOFunctionsX.py
#  Discription  : File handeling in python
#  Author       : Apurva Vilas Shinde
#  Date         : 16/06/2026
#
##################################################################################################################

import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        fobj = open(FileName,"w")

        print(fobj.readable())   
        print(fobj.writable())   
        print(fobj.seekable()) 

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()