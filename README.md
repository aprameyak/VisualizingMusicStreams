# 📊 Track Score vs Playlist Count Analysis

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)  
![Pandas](https://img.shields.io/badge/Library-Pandas-green?logo=pandas)  
![Scipy](https://img.shields.io/badge/Library-Scipy-lightgreen?logo=scipy)  
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-red?logo=matplotlib)  

## 📌 What it Does  

The **Track Score vs Playlist Count Analysis** project explores the relationship between track scores and playlist counts on three major music streaming platforms: **Apple Music**, **Amazon Music**, and **Deezer**. By calculating Pearson’s correlation coefficient, it provides insights into how the track score is related to the number of playlists the track is featured in on each platform. The results are visualized with line graphs, showcasing the data and correlation values.

## 🚀 How We Built It  

### Technologies Used:  
- **Python**: A powerful programming language used for data processing and analysis.  
- **Pandas**: A Python library used for data manipulation and analysis.  
- **Scipy**: A library used for scientific and statistical computations, including Pearson’s correlation.  
- **Matplotlib**: A library for creating static, animated, and interactive visualizations in Python.  

### Data Preprocessing:  
- **CSV File (`MostStreamed.csv`)**: Contains data on track scores and playlist counts across the three platforms.  
- **Handling Missing Data**: Missing values in playlist count columns were filled with `0` to maintain the integrity of the dataset.  

### Visualization:  
- **Line Plot**: Created to display the relationship between track scores and playlist counts for each platform.  
- **Correlation Values**: Pearson's correlation coefficients for each platform were calculated and displayed on the plot.

## 🚀 Features  

- **Data Processing**: Cleans and processes the dataset, filling missing playlist counts.  
- **Correlation Analysis**: Calculates Pearson’s correlation coefficients to measure the strength of relationships between track scores and playlist counts.  
- **Interactive Visualization**: Displays a line plot visualizing playlist count vs. track score for Apple Music, Amazon Music, and Deezer.  
- **Correlation Annotations**: Displays the calculated correlation coefficients on the plot for each platform.  

### Interactive Features:
- **Dynamic Plot**: Updates with track score and playlist count data from the CSV file.  
- **Correlation Insights**: Shows real-time Pearson correlation values as part of the visual output.  

## 🔗 Integration  

- **Pandas**: Used for data handling and preprocessing.  
- **Scipy**: Used to calculate Pearson's correlation coefficient between track scores and playlist counts.  
- **Matplotlib**: Used for creating the line plot and rendering visual data.  

