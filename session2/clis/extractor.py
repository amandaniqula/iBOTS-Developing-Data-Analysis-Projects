import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description="extractor")

parser.add_argument('input', type=str, help='raw data')
parser.add_argument('output', type=str, help='extracted data')

args = parser.parse_args()

# Load the csv file and extract active trials
df = pd.read_csv(input_csv_path)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(output_csv_path, index=False)

