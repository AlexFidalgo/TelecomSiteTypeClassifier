import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from clean_data_for_decision_tree import *

def CreateDecisionTree(anatel_file_path, test_size, random_state, criterion, max_depth, min_samples_split, min_samples_leaf):

    anatel = pd.read_csv(anatel_file_path)

    get_rid_of_problematic_columns(anatel)

    rename_anatel_cols(df)

    # Treatment of Null values
    df = df.dropna()

    # One-Hot Encoding
    anatel = pd.get_dummies(anatel, columns=['Polarization'], prefix='Polarization')
    anatel = pd.get_dummies(anatel, columns=['BasicFeatures'], prefix='BasicFeatures')
    # Decision trees and random forests can handle boolean variables without encoding. They naturally make binary decisions based on the values of the features.

    # Station as the index
    df['Station'] = df['Station'].astype(int)
    anatel.set_index('Station', inplace=True)

    # Split data into features and target
    X = anatel.drop("SiteType", axis=1)
    y = anatel["SiteType"]

    # Split Data into Training and Testing Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Build and Train the Decision Tree Model
    tree_model = DecisionTreeClassifier(random_state=random_state, criterion=criterion, max_depth=max_depth, 
                                        min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf)
    tree_model.fit(X_train, y_train)

    # Use the trained model to make predictions on the test set
    y_pred = tree_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    classification_report = classification_report(y_test, y_pred)

    return accuracy, classification_report


if __name__ == '__main__':

    # Proportion of the dataset to include in the test split
    test_size = 0.2
    # Controls the shuffling applied to the data before applying the split (pass int for reproducible output across multiple function 
    # calls)
    random_state = 42
    # The function to measure the quality of a split. Supported criteria are “gini” for the Gini impurity and “log_loss” and “entropy” 
    # both for the Shannon information gain
    criterion = 'gini'
    # The maximum depth of the tree. i=If None, then nodes are expanded until all leaves are pure or until all leaves contain less than 
    # min_samples_split samples
    max_depth = None
    # The minimum number of samples required to split an internal node
    min_samples_split = 2
    # The minimum number of samples required to be at a leaf node. A split point at any depth will only be considered if it leaves at 
    # least min_samples_leaf training samples in each of the left and right branches.
    min_samples_leaf = 1

    # Find anatel file path
    script_directory = os.path.dirname(os.path.realpath(__file__)) # directory of this script
    script_directory_parent2 = os.path.dirname(os.path.dirname(script_directory)) # parent of the directory of the script
    anatel_file_path = os.path.join(script_directory_parent2, 'data', 'labeled_csv_files', 'Anatel_labeled.csv')

    accuracy, classification_report = CreateDecisionTree(anatel_file_path, test_size, random_state, criterion, 
                                                         max_depth, min_samples_split, min_samples_leaf)

    print(f"Accuracy: {accuracy}")
    print(f"Classification Report: {classification_report}")

