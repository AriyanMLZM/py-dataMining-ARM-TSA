from .. import draw_line
import pandas as PD
import os


def clean_data(dataset, output_path):
  draw_line("Cleaning Data")

  initial_rows = len(dataset)

  # Handle missing values: Remove rows with missing Description
  dataset.dropna(subset=['Description'], inplace=True)

  # Remove invalid records (non-positive Quantity/UnitPrice)
  df_clean = dataset[(dataset['Quantity'] > 0) &
                     (dataset['UnitPrice'] > 0)].copy()

  # Data type conversion: Convert InvoiceDate to datetime format
  df_clean['InvoiceDate'] = PD.to_datetime(
      df_clean['InvoiceDate'], errors='coerce')
  df_clean.dropna(subset=['InvoiceDate'], inplace=True)

  # Feature engineering: Create TotalAmount
  df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']

  # Save
  df_clean.to_csv(os.path.join(
      output_path, 'cleaned_data.csv'), index=False)

  print(
      f"Saved cleaned data to {os.path.join(output_path, 'cleaned_data.csv')}")
  print(
      f"Initial Records: {initial_rows}. Final Clean Records: {len(df_clean)}.")
  print("\nFist five records of cleaned data:")
  print(df_clean.head(5))

  return df_clean
