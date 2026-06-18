##################################################################################################################
#
#  Program Name : 128_FileIOExceptionReadSeekXX.py
#  Discription  : File handeling in python
#  Author       : Apurva Vilas Shinde
#  Date         : 16/06/2026
#
##################################################################################################################

def main():
    try:
        fobj = open("Hello.txt","r")
        print("File gets succsesfully opened")

        print("Current offset is : ",fobj.tell())   # 0

        fobj.seek(6,0)

        print("Current offset is : ",fobj.tell())  # 11

        Data = fobj.read(6)

        print("Current offset is : ",fobj.tell())   # 17

        print("Data from file is : ",Data)

        fobj.close()
    
    except FileNotFoundError:
        print("Unalble to open filr as there is no such file")

    finally:
        print("End of application")


if __name__ == "__main__":
    main()