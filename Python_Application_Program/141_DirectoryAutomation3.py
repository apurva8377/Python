##################################################################################################################
#
#  Program Name : 141_DirectoryAutomation3.py
#  Discription  : Automation
#  Author       : Apurva Vilas Shinde
#  Date         : 18/06/2026
#
##################################################################################################################

import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Thre is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName, Filename in os.walk(DirName):
        for fname in Filename:
            fname = os.path.join(FolderName, fname)
            print("File name : ",fname)
            print("File Size : ",os.path.getsize(fname))


def main():
    Border = "-"*60

    print(Border)
    print("-----------------------Marvellous Directory Scanner----------------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()