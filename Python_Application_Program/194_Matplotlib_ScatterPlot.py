##################################################################################################################
#
#  Program Name : 194_Matplotlib_CountPlot.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

def main():

    #Linear relationship (freatures)
    sns.scatterplot(x= [1,2,3], y=[3,1,4])

    plt.show()

if __name__ == "__main__":
    main()