##################################################################################################################
#
#  Program Name : 121_FileIOExceptionWriteX.py
#  Discription  : Automation program
#  Author       : Apurva Vilas Shinde
#  Date         : 14/06/2026
#
##################################################################################################################

def main():
    try:
        fobj = open("Hello.txt","w")
        print("File gets succsesfully opened")

        fobj.write("Jay Ganesh Marvellous...")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as thre is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()