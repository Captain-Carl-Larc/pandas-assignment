import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Load and Explore the Dataset
# 1. Load the dataset
dataset_path = r"./data/iris.data"  # Updated path

try:
    # Attempt to read as CSV first
    df = pd.read_csv(dataset_path, header=None) 
    # print(f"Dataset successfully loaded from {dataset_path} as CSV")
except Exception as e:
    print(f"Error loading CSV: {e}")    
    print(f"Could not load dataset from {dataset_path}.  Please make sure the path is correct and the file is a supported format (CSV, text).")

# 2. Display the first few rows of the dataset
# print(df.head())

# 3. Explore the structure of the dataset
# print(df.info())

# 4. Check for missing values
nullValues = df.isnull().sum()
# print(nullValues)

def drop_null_values(df):
    return df.dropna()

if nullValues.any():
    # print("Dataset contains missing values.")
    df = drop_null_values(df)
else:
    pass
    # print("Dataset does not contain missing values.")


# Task 2: Basic Data Analysis
# Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
print(df.describe())

# Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
# Identify any patterns or interesting findings from your analysis.
