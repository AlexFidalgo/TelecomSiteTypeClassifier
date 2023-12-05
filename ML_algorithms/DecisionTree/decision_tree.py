import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

def CreateDecisionTree(anatel_file_path, test_size, random_state, criterion, max_depth, min_samples_split, min_samples_leaf):

    anatel = pd.read_csv(anatel_file_path)

    # One-Hot Encoding
    anatel = pd.get_dummies(anatel, columns=['Polarization'], prefix='Polarization')
    anatel = pd.get_dummies(anatel, columns=['BasicFeatures'], prefix='BasicFeatures')
    # Decision trees and random forests can handle boolean variables without encoding. They naturally make binary decisions based on the values of the features.

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
    cr = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"Classification Report: {classification_report}")

    cm = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:\n", cm)

    feature_importances = tree_model.feature_importances_
    print("Feature Importances:\n", feature_importances)

    scores = cross_val_score(tree_model, X, y, cv=5)
    print("Cross-Validation Scores:", scores)

    param_grid = {
        'criterion': ['gini', 'entropy'],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    grid_search = GridSearchCV(tree_model, param_grid, cv=5)
    grid_search.fit(X, y)
    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)




