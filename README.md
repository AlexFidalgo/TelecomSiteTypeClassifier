# Telecom Site Type Classifier

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

A machine learning project that predicts telecom site types: rooftop, greenfield, indoor, or street-level.

## Overview

The Telecom Site Type Classifier project utilizes machine learning techniques to predict the type of telecom sites, including rooftops, greenfields, and others. The goal is to automate the site type classification process based on relevant features.

## Getting Started

1. Clone this repository:

   ```shell
   git clone https://github.com/AlexFidalgo/TelecomSiteTypeClassifier.git
   cd TelecomSiteTypeClassifier
   ```

2. Install the necessary dependencies (Python and required libraries).

3. Create a folder named `data`  


4. Run the `main.py` script to download and preprocess the dataset:

   ```shell
   python main.py
   ```

   The `main.py` script will perform the following steps:
   - Create a directory named `data` at the main location of the project.
   - Execute the `download.ps1` PowerShell script, which downloads all data from [Anatel](https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php?view=licenciamento) into zip files in the `zip_files` directory.
   - Unzip these files to CSV files under the `csv_files` directory.
   - Delete the downloaded zip files.

5. Explore the data using the `explore_data.ipynb` Jupyter notebook.


## Acknowledgments

Thanks to Anatel for providing the dataset for this project.

## Author

Alex Fidalgo

## Connect with Me

LinkedIn: [Alex Fidalgo](https://www.linkedin.com/in/alex-zamikhowsky/)


