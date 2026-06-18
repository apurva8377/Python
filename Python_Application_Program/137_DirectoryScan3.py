##################################################################################################################
#
#  Program Name : 136_DirectoryScan2.py
#  Discription  : File handeling in python
#  Author       : Apurva Vilas Shinde
#  Date         : 17/06/2026
#
##################################################################################################################

import os

def DirectoryScanner(DirectoryName = "Marvellous"):
    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Thre is no such directory")
        return
    
    print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)

        for subf in SubFolderName:
            print("SubFolder name : ",subf)

        for fname in FileName:
            print("File name : ",fname)

def main():
    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()