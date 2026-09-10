##################################################################################################################
#
#  Program Name : 186_Pandas_Series5.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import pandas as pd

def main():
    sobj = pd.Series([25000,27000,29000,30000], index=["PPA","LB","Python","React"])

    print(sobj)

    print(sobj["Python"])

if __name__ == "__main__":
    main()