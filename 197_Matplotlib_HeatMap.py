##################################################################################################################
#
#  Program Name : 197_Matplotlib_HeatMap.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():

    dobj = pd.DataFrame({
        "A" : [1,2,3],
        "B" : [4,5,6],
        "C" : [7,8,9]
    })

    print(dobj)

    #Feature Correlation
    sns.heatmap(dobj.corr(), annot=True)

    plt.show()

if __name__ == "__main__":
    main()