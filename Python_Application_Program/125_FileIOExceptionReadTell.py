##################################################################################################################
#
#  Program Name : 125_FileIOExceptionReadTell.py
#  Discription  : Automation program
#  Author       : Apurva Vilas Shinde
#  Date         : 14/06/2026
#
##################################################################################################################

def main():
    try:
        fobj = open("Hello.txt","r")
        print("File gets succesfully opened")
        
        print("Current offset is : ",fobj.tell())

        Data = fobj.read(6)

        print("Current offset is : ",fobj.tell())

        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as thre is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()