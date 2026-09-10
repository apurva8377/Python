##################################################################################################################
#
#  Program Name : 188_Pandas_Dataframe2.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import pandas as pd

def main():
    Data = {
        "Name" : ["Sager","Amit","Pooja"],
        "Age"  : [23,26,25],
        "City" : ["Pune","Mumbai","Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj)

    print(dobj["Age"])

    print(dobj["City"])

if __name__ == "__main__":
    main()