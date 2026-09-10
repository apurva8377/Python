##################################################################################################################
#
#  Program Name : 193_Matplotlib_CountPlot.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Categorical data
    sns.countplot(x= ["A","B","A","A","B","A","C"])

    plt.show()

if __name__ == "__main__":
    main()