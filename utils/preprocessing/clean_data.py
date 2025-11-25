from .. import draw_line
import pandas as PD


def clean_data(dataset):
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

  print(
      f"Initial Records: {initial_rows}. Final Clean Records: {len(df_clean)}.")
  return df_clean
