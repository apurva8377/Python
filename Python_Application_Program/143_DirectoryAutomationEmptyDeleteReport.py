##################################################################################################################
#
#  Program Name : 142_DirectoryAutomationEmptyDeleteReport.py
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
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFoldername, FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName, fname)
            print("file name : ",fname)
            print("File size : ",os.path.getsize(fname))

            #  Empty file
            if(os.path.getsize(fname) == 0):
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    Border = "-"*60
    print(Border)

def main():
    Border = "-"*60

    print(Border)
    print("--------------Marvellous Directory Automation-------------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])

    print(Border)
    print("-----------------Marvellous Directory Automation------------------")
    print(Border)
    
if __name__ == "__main__":
    main()