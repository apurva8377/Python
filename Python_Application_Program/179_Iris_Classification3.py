##################################################################################################################
#
#  Program Name : 179_Iris_Classification3.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

from sklearn.datasets import load_iris

def main():
    print("Iris classification case study")

    Dataset = load_iris()

    # Metadata of dataset
    print("Independent variables are : ")
    print(Dataset.feature_names)
    print("Length of Independent variables is : ",len(Dataset.feature_names))

    print("Dependent variable are : ")
    print(Dataset.target_names)
    print("Length of dependent variables is : ",len(Dataset.target_names))

if __name__ == "__main__":
    main()