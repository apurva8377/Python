##################################################################################################################
#
#  Program Name : 135_DirectoryScan1.py
#  Discription  : File handeling in python
#  Author       : Apurva Vilas Shinde
#  Date         : 17/06/2026
#
##################################################################################################################

import os

def main():
    DirectoryName = input("Enter the name of directory : ")

    print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("FolderName : ",FolderName)

        for subf in SubFolderName:
            print("SubFolder name : ",subf)
        
        for fname in FileName:
            print("File name : ",fname)

if __name__ == "__main__":
    main()