# Telecom Site Type Classifier

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

A project that predicts telecom site types based on all Brazilian telecom stations data from Anatel, using machine learning.

## Abstract

The Telecom Site Type Classifier project is a machine learning initiative that endeavors to predict various types of telecom sites in Brazil using data sourced from the Brazilian National Telecommunications Agency (Anatel). Targeting site classifications such as GREENFIELD, ROOFTOP, RAN SHARING, STREETLEVEL, INDOOR, OUTDOOR, HARMONIZADA, SMALLCELL, COW, and FASTSITE, the project seeks to automate and enhance the efficiency of the telecom site classification process. By leveraging relevant features extracted from the Anatel dataset, the project contributes to a deeper understanding of the Brazilian telecom landscape. Users can engage with the project by cloning the repository, installing dependencies, and executing provided scripts for dataset preprocessing, transformation, and exploration.
**Keywords:** Telecom Site Classification, Machine Learning, Anatel Dataset, Decision Tree Model, Data Exploration, Automation, Brazilian Telecommunications.


## Overview

The Telecom Site Type Classifier project utilizes machine learning techniques to predict the type of telecom sites present in Brazil:
- GREENFIELD     
- ROOFTOP        
- RAN SHARING     
- STREETLEVEL      
- INDOOR 
- OUTDOOR           
- HARMONIZADA         
- SMALLCELL   
- COW
- FASTSITE
The goal is to automate the site type classification process based on relevant features found in the Anatel data.

## Getting Started

1. Clone this repository:

   ```shell
   git clone https://github.com/AlexFidalgo/TelecomSiteTypeClassifier.git
   cd TelecomSiteTypeClassifier
   ```

2. Install the necessary dependencies (Python and required libraries).

3. Run the `notebooks/main.py` script to download and preprocess the dataset:

   ```shell
   python main.py
   ```

   The `main.py` script will perform the following steps:
   - Create a directory named `data` at the main location of the project.
   - Execute the `download.ps1` PowerShell script, which downloads all data from [Anatel](https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php?view=licenciamento) into zip files in the `zip_files` directory, one state at a time (which is a requirement imposed by the website).
   - Unzip these files to CSV files under the `csv_files` directory.
   - Delete the downloaded zip files.
   - Execute the `transform_data.py` script, which processes the columns.
   - Execute the `aggregate_data.py` script, which appropriately groups the data by station.

4. Explore the data using the `explore_data.ipynb` Jupyter notebook.

## Running Machine Learning Analyses

1. Run `ML_algorithms/DecisionTree/decision_tree.py` to perform a classification based on the Decision Tree model. You may explore it and play with the parameters and features by using the `DecisionTree/visualizer.ipynb`





## Author

Alex Fidalgo

## Connect with Me

LinkedIn: [Alex Fidalgo](https://www.linkedin.com/in/alex-zamikhowsky/)


