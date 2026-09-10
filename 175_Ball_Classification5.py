##################################################################################################################
#
#  Program Name : 175_Ball_Classification5.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################
from sklearn import tree

# Tennis = 1
# Cricket = 2

def main():
    print("Ball classification case study")

    # Original encoded dataset
    # Independent variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Dependent variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independent variable for training
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,1],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]

    # Independent variables for testing
    Xtest = [[35,1],[95,0]]

    # Dependent variable for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]

    # Dependent variable for testing

    Ytest = [1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain, Ytrain)

    Result = trainedmodel.predict(Xtest)  # 1    2

    print("Mosel predicts the object as : ",Result)

if __name__ == "__main__":
    main()

# Dataset Size : 15
