##################################################################################################################
#
#  Program Name : 190_Pandas_Dataframe4.py
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

    # Fetch specific row
    print(dobj.loc[0])

if __name__ == "__main__":
    main()