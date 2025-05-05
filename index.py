import pandas as pd

# Task 1: Load and Explore the Dataset
# 1. Load the dataset
dataset_path = r"C:\Users\kalwe\Downloads\iris\iris.data"  # Updated path

try:
    # Attempt to read as CSV first
    df = pd.read_csv(dataset_path, header=None) 
    print(f"Dataset successfully loaded from {dataset_path} as CSV")
except Exception as e:
    print(f"Error loading CSV: {e}")    
    print(f"Could not load dataset from {dataset_path}.  Please make sure the path is correct and the file is a supported format (CSV, text).")

# 2. Display the first few rows of the dataset
print(df.head())