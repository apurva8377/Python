##################################################################################################################
#
#  Program Name : 196_Matplotlib_BoxPlot.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Detecting outliers
    sns.boxplot(x= [10,20,30,110])

    plt.show()

if __name__ == "__main__":
    main()