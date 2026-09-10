##################################################################################################################
#
#  Program Name : 177_Iris_Classification1.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

from sklearn.datasets import load_iris

def main():
    print("Iris classification case study")

    Dataset = load_iris()

    print(Dataset)

if __name__ == "__main__":
    main()