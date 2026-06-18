##################################################################################################################
#
#  Program Name : 140_DirectoryAutomation2.py
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
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            print("File name : ",fname)
            print("File size : ",os.path.getsize(fname))    # path issue

def main():

    Border = "-"
    
    print(Border)
    print("-----------------Marvellous Directory Automation-----------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()