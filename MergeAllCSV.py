import os
import pandas as pd

# Path to the folder containing all CSV files
folder_path = 'All_CSV'

# List to store DataFrames from each CSV file
dfs = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('mydataset.csv', index=False)

print("Merging and writing to mydataset.csv completed.")
