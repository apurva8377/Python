##################################################################################################################
#
#  Program Name : 122_FileIOExceptionAppend.py
#  Discription  : Automation program
#  Author       : Apurva Vilas Shinde
#  Date         : 14/06/2026
#
##################################################################################################################

def main():
    try:
        fobj = open("Hello.txt","a")
        print("File gets succsesfully opened")

        fobj.write("Python Automation")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as thre is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()