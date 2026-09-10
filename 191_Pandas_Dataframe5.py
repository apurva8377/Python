##################################################################################################################
#
#  Program Name : 191_Pandas_Dataframe5.py
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

    
    print(dobj.loc[:,"Name"])

if __name__ == "__main__":
    main()