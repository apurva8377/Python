##################################################################################################################
#
#  Program Name : 173_Ball_Classification3.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################
from sklearn import tree

# Rough = 1
# Smooth = 0

# Tennis = 1
# Cricket = 2

def main():
    print("Ball classification case study")

    # Independent variables
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Dependent variables
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Features, Labels)

    Result = trainedmodel.predict([[37,1],[94,0]])  # 1    2

    print("Mosel predicts the object as : ",Result)

if __name__ == "__main__":
    main()

# Dataset Size : 15
