# Telecom Site Type Classifier

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

A machine learning project that predicts telecom site types such as rooftops, greenfields, and more.

## Overview

The Telecom Site Type Classifier project utilizes machine learning techniques to predict the type of telecom sites, including rooftops, greenfields, and others. The goal is to automate the site type classification process based on relevant features.

## Getting Started

1. Clone this repository:

   ```shell
   git clone https://github.com/AlexFidalgo/TelecomSiteTypeClassifier.git
   cd TelecomSiteTypeClassifier
   ```

3. Install the necessary dependencies (Python and required libraries).

3. Run the `main.py` script to download and preprocess the dataset:

   ```shell
   python main.py
   ```

   The `main.py` script will execute the `download.ps1` PowerShell script, which downloads all data from [Anatel](https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php?view=licenciamento) into zip files in the `zip_files` directory. Then, it will unzip these files to CSV files under the `csv_files` directory and delete the zip files.

4. Explore the data using the `explore_data.ipynb` Jupyter notebook.


## Acknowledgments

Thanks to Anatel for providing the dataset for this project.

## Author

Alex Fidalgo

## Connect with Me

LinkedIn: [Alex Fidalgo](https://www.linkedin.com/in/alex-zamikhowsky/)


