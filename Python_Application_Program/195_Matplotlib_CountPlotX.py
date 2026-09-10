##################################################################################################################
#
#  Program Name : 195_Matplotlib_CountPlotX.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

def main():

    sns.countplot(x= ["C","C","C++","Java","C++","Python","Javascript","C++","Golang","C"])

    plt.show()

if __name__ == "__main__":
    main()