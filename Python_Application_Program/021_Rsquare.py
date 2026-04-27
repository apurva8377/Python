############################################
#
#  Program Name : 21_Rsquare.py
#  Discription  :Write a Python program to calculate the R-square (coefficient of determination) value using actual and predicted data.
#  Auther       : Apurva Vilas Shinde
#  Date         : 27/04/2026
#
############################################

from sklearn.metrics import r2_score

def main():
    Y_actual = [3,4,2,4,5]
    Y_predicted = [2.8,3.2,3.6,4.0,4.4]

    r2 = r2_score(Y_actual,Y_predicted)

    print("Actual values are : ",Y_actual)
    print("Predicted values are : ",Y_predicted)
    print("R square value : ",r2)   # 0.307

if __name__ == "__main__":
    main()