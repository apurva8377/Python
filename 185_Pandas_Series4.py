##################################################################################################################
#
#  Program Name : 185_Pandas_Series4.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import pandas as pd

def main():
    sobj = pd.Series([11.0,21.0,51.0,101.0,111.0], index=[5,6,7,8,9])

    print(sobj)

    print(sobj[7])

if __name__ == "__main__":
    main()