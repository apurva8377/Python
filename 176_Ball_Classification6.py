##################################################################################################################
#
#  Program Name : 176_Ball_Classification6.py
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

    Result = trainedmodel.predict([[35,1]])  

    print(type(Result))

    if Result == 1:
        print("Object looks like tennis ball")
    elif Result == 2:
        print("Object looks like cricket ball")

if __name__ == "__main__":
    main()

# Dataset Size : 15
