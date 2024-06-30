# Introduction to Data Preprocessing

In the real world, data comes from multiple sources of acquisition and collection and can contain anomalies or incorrect values that compromise their quality. The most common data quality issues include:

- **Incomplete data**: Missing values or attributes.
- **Noisy data**: The data contains erroneous individuals or outliers.
- **Redundancy**: The data is high-dimensional and contains unnecessary information.

Good data quality is essential for obtaining high-performance AI systems. To avoid developing models with poor-quality data, it is imperative to analyze the data, detect anomalies, and determine the appropriate preprocessing and cleaning steps.

## Why Preprocess Data?

Data preprocessing is necessary to address various issues that arise from raw data. The main operations involved in data preprocessing include:

- **Data Cleaning**: Handling missing values and outliers.
- **Data Transformation**: Normalization and standardization.
- **Data Encoding**: Converting categorical data into numerical form.
- **Dimensionality Reduction**: Feature extraction and feature selection.

## Main Data Preprocessing Operations

Here are the primary operations involved in data preprocessing:

| Data Cleaning                | Data Encoding          | Normalization & Standardization    | Feature Extraction         |
|------------------------------|------------------------|------------------------------------|----------------------------|
| - Missing data               | - One-hot encoding     | - Normalization (e.g., MinMaxScaler) | - Feature extraction       |
| - Outliers                   | - Label encoding       | - Standardization (e.g., StandardScaler) | - Feature selection       |
