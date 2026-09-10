##################################################################################################################
#
#  Program Name : 192_Matplotlib_Histogram.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Contiguos values
    sns.histplot(data= [10,20,30,20,20,20,30,40])

    plt.show()

if __name__ == "__main__":
    main()