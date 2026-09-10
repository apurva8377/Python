##################################################################################################################
#
#  Program Name : 199_CaseStudyStep2.py
#  Discription  : Data Science with Machine Learning
#  Author       : Apurva Vilas Shinde
#  Date         : 06/09/2026
#
##################################################################################################################

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

#########################################################
# Step 1 : Load the dataset
#########################################################
print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset : ")
print(df.head())

#########################################################
# Step 2 : Data Analysis (EDA)
#########################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing values (per column)")
print(df.isnull().sum())

print("Class Distribution (Variety count)")
print(df["variety"].value_counts())

print("statistical Report of datset")
print(df.describe())