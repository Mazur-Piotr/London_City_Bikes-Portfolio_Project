# London City Bikes Data Cleaning and Transformation
## Overview
This project focuses on the thorough cleaning and transformation of London City Bikes data. The main objective is to prepare the dataset for further analysis and visualization by addressing data quality issues and refining column values.

## Project Structure
### 1. Extracted Dataset from Kaggle
### 2. Data Import and Cleaning
- Imported essential Python modules, including Pandas, Zipfile, and OS.
- Configured the working directory for data handling.
- Extracted data from the downloaded zip file.
- Loaded the bike-sharing data from a CSV file into a Pandas DataFrame.
- Conducted initial data exploration, including checking data types and null values.
### 2. Data Transformation
- Renamed columns for improved clarity and understanding.
- Adjusted humidity values to a percentage format (between 0 and 1).
- Created dictionaries to map numeric codes to descriptive values for the 'season' and 'weather' columns.
- Converted data types of 'season' and 'weather' columns to strings.
- Mapped numeric codes to meaningful season and weather descriptions.
- Transformed and cleaned data for further analysis.
- Prepared the final transformed dataset for visualization by exporting it to an Excel file.
### 3. Loaded Data to Tableau 
### 4. Data Visualization
- Utilized data visualization tools such as Tableau to create insightful visualizations (not included in this code snippet).
## Technologies Used
- Python
- Pandas
- Tableau
## Usage
This project provides a foundational understanding of the data cleaning and transformation process required for subsequent data analysis and visualization tasks related to London City Bikes data
