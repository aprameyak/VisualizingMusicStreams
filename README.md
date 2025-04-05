# Visualizing Music Streams

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white&style=for-the-badge)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white&style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white&style=for-the-badge)

## About

**Visualizing Music Streams** explores the relationship between track scores and playlist counts on three major music streaming platforms: **Apple Music**, **Amazon Music**, and **Deezer**. By calculating **Pearson’s correlation coefficient**, the project provides insight into how track popularity correlates with playlist exposure.

## Features

- **Data Preprocessing**: Handles missing values in playlist columns by filling with `0`  
- **Correlation Analysis**: Calculates Pearson’s r to evaluate strength of linear relationships  
- **Visual Insight**: Generates clear line plots showing the relationship per platform  
- **Correlation Annotations**: Displays correlation values directly on the plot

### Platforms Analyzed:
- Apple Music  
- Amazon Music  
- Deezer

## Technology Stack

- **Language**: Python  
- **Libraries**:
  - **Pandas** – for data loading, cleaning, and manipulation  
  - **SciPy** – for Pearson correlation coefficient calculation  
  - **Matplotlib** – for creating line plots and displaying results

## Data

- **Source**: `MostStreamed.csv`  
- **Contents**:
  - `track_score`  
  - `apple_playlist_count`  
  - `amazon_playlist_count`  
  - `deezer_playlist_count`

## Workflow

1. Load and clean data with Pandas  
2. Fill missing values in playlist columns with `0`  
3. Calculate correlation between track score and playlist counts per platform  
4. Visualize all three results using a single line plot  
5. Annotate correlation values on the graph for clarity
