##################################################################################################################
#
#  Program Name : 148_CheckSumCalculate.py
#  Discription  : Automation
#  Author       : Apurva Vilas Shinde
#  Date         : 18/06/2026
#
##################################################################################################################

import hashlib

def CalculateCheckSum(Filename):
    fobj = open(Filename,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def main():
    Ret = CalculateCheckSum("Demo.txt")

    print("CheckSum is : ",Ret)

if __name__ == "__main__":
    main()