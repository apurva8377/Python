##################################################################################################################
#
#  Program Name : 183_Pandas_Series1.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import pandas as pd

def main():
    Data = [11,21,51,101,111]

    print(Data)

    sobj = pd.Series(Data)

    print(sobj)

if __name__ == "__main__":
    main()