##################################################################################################################
#
#  Program Name : 182_Confusion_Matrix.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

from sklearn.metrics import confusion_matrix

def main():
    # 1 : Positive
    # 0 : Negative

    Actual =    [1,0,1,1,1,0,1,0,0,1]
    Predicted = [1,0,0,1,1,1,1,1,0,1]

    print("Actual Data : ",Actual)
    print("Predicted Data : ",Predicted)

    con_mat = confusion_matrix(Actual, Predicted)

    print(con_mat)

if __name__ == "__main__":
    main()