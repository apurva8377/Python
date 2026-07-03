##################################################################################################################
#
#  Program Name : 149_CheckSumCalculateDirectory.py
#  Discription  : Automation
#  Author       : Apurva Vilas Shinde
#  Date         : 1/07/2026
#
##################################################################################################################

import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectWatcher(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    for Foldername, SubFolderName, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(Foldername,fname)

            CheckSum = CalculateCheckSum(fname)

            print(f"File name : {fname}")
            print(f"Check sum = {CheckSum}")

def main():
    DirectWatcher()

if __name__ == "__main__":
    main()