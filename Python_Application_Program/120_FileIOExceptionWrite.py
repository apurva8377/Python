##################################################################################################################
#
#  Program Name : 120_FileIOExceptionWrite.py
#  Discription  : Automation program
#  Author       : Apurva Vilas Shinde
#  Date         : 14/06/2026
#
##################################################################################################################

def main():
    try:
        open("Demo.txt","w")
        print("File gets succsesfully opened")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()