##################################################################################################################
#
#  Program Name : 109_CommandLine3.py
#  Discription  : Command Line 
#  Author       : Apurva Vilas Shinde
#  Date         : 13/06/2026
#
##################################################################################################################

import sys

def main():
    print("Command line arguments are : ")

    for i in range(len(sys.argv)):
        print(sys.argv[i])
    
if __name__ == "__main__":
    main()