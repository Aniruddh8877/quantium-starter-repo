import pandas as pd
import glob
import os

data_folder = './data'  # folder where your CSV files are
output_file = 'combined_sales.csv'

# Find all CSV files in the folder
csv_files = glob.glob(os.path.join(data_folder, '*.csv'))

# List to store processed DataFrames
processed_dfs = []

for file in csv_files:
    df = pd.read_csv(file)  # read the current file in the loop
    
    # Keep only Pink Morsels
    df = df[df['product'] == 'Pink Morsel']
    
    # Compute total sales
    df['Sales'] = df['quantity'] * df['price']
    
    # Keep only required columns and rename them
    df = df[['Sales', 'date', 'region']].rename(columns={'date': 'Date', 'region': 'Region'})
    
    processed_dfs.append(df)

# Combine all files
combined_df = pd.concat(processed_dfs, ignore_index=True)

# Convert Date to datetime and sort
combined_df['Date'] = pd.to_datetime(combined_df['Date'])
combined_df.sort_values('Date', inplace=True)

# Save to a single CSV file
combined_df.to_csv(output_file, index=False)

print(f"Combined and formatted sales data saved to {output_file}")
