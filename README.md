# Telecom Site Type Classifier

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

A project that predicts telecom site types (Greenfield, Streetlevel, Ran Sharing, Small Cell, COW, Picocell, Harmonized, Rooftop, Indoor, and Outdoor) based on all Brazilian telecom stations data from Anatel, using machine learning.

## Overview

The Telecom Site Type Classifier project utilizes machine learning techniques to predict the type of telecom sites, including rooftops, greenfields, and others in Brazil. The goal is to automate the site type classification process based on relevant features found in the Anatel data.

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
   - Execute the `download.ps1` PowerShell script, which downloads all data from [Anatel](https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php?view=licenciamento) into zip files in the `zip_files` directory.
   - Unzip these files to CSV files under the `csv_files` directory.
   - Delete the downloaded zip files.

4. Explore the data using the `explore_data.ipynb` Jupyter notebook.

5. Perform data treatment by running  `transform_data.py`.

## Running Machine Learning Analyses




## Acknowledgments

Thanks to Anatel for providing the dataset for this project.

## Author

Alex Fidalgo

## Connect with Me

LinkedIn: [Alex Fidalgo](https://www.linkedin.com/in/alex-zamikhowsky/)


