import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from clean_data_for_decision_tree import *

# Find anatel file path
script_directory = os.path.dirname(os.path.realpath(__file__)) # directory of this script
script_directory_parent2 = os.path.dirname(os.path.dirname(script_directory)) # parent of the directory of the script
anatel_file_path = os.path.join(script_directory_parent2, 'data', 'labeled_csv_files', 'Anatel_labeled.csv')

anatel = pd.read_csv(anatel_file_path)

get_rid_of_problematic_columns(anatel)

rename_anatel_cols(df)

# Treatment of Null values
df = df.dropna()

# One-Hot Encoding
anatel = pd.get_dummies(anatel, columns=['Polarization'], prefix='Polarization')
anatel = pd.get_dummies(anatel, columns=['BasicFeatures'], prefix='BasicFeatures')

# Station as the index
df['Station'] = df['Station'].astype(int)
anatel.set_index('Station', inplace=True)

# Split data into features and target
X = anatel.drop("SiteType", axis=1)
y = anatel["SiteType"]

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and Train the Decision Tree Model
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Use the trained model to make predictions on the test set
y_pred = tree_model.predict(X_test)

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))



