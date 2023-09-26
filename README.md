# London City Bikes Data Cleaning and Transformation
## Overview
This project focuses on the thorough cleaning and transformation of London City Bikes data. The main objective is to prepare the dataset for further analysis and visualization by addressing data quality issues and refining column values.
## Dataset
Dataset Source: Kaggle - <br>
https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset <br> <br>
The dataset consists of historical data for bike sharing in London 'Powered by TfL Open Data'.

| Column        | Non-Null Count | Dtype    |
| ------------- | --------------- | ------- |
| timestamp     | 17414 non-null | object  |
| cnt           | 17414 non-null | int64   |
| t1            | 17414 non-null | float64 |
| t2            | 17414 non-null | float64 |
| hum           | 17414 non-null | float64 |
| wind_speed    | 17414 non-null | float64 |
| weather_code  | 17414 non-null | float64 |
| is_holiday    | 17414 non-null | float64 |
| is_weekend    | 17414 non-null | float64 |
| season        | 17414 non-null | float64 |

## Project Structure
### 1. Extracted Dataset from Kaggle
### 2. Data Import and Cleaning
- Imported essential Python modules, including Pandas, Zipfile, and OS.
- Configured the working directory for data handling.
- Extracted data from the downloaded zip file.
- Loaded the bike-sharing data from a CSV file into a Pandas DataFrame.
- Conducted initial data exploration, including checking data types and null values, using .shape, .info., value_counts().
### 3. Data Transformation
- Renamed columns for improved clarity and understanding.
- Adjusted humidity values to a percentage format (between 0 and 1).
- Created dictionaries to map numeric codes to descriptive values for the 'season' and 'weather' columns.
- Converted data types of 'season' and 'weather' columns to strings.
- Mapped numeric codes to meaningful season and weather descriptions.
- Transformed and cleaned data for further analysis.
- Prepared the final transformed dataset for visualization by exporting it to an Excel file.
### 4. Loaded Data to Tableau 
### 5. Data Visualization
- Utilized data visualization tools such as Tableau to create insightful visualizations (not included in this code snippet).
- Used advanced methods, such as Creating Calculated Fields and Paramateres to create Moving Avarage Period with period customized by user<br>

  ![image](https://github.com/Mazur-Piotr/London_City_Bikes-Portfolio_Project/assets/138219323/2c1b2512-6048-4fb6-a5cd-9628a213ae85)

  <br>
## Technologies Used
- Python: Pandas, Zipfile, OS 
- Tableau
## Usage
This project provides a foundational understanding of the data cleaning and transformation process required for subsequent data analysis and visualization tasks related to London City Bikes data
