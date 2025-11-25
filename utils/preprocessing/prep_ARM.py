import os
from .. import draw_line


def prep_ARM(dataset, outputPath):
  draw_line("Preprocessing for Association Rule Mining")

  df_arm = dataset.copy()
  df_arm['Description'] = df_arm['Description'].astype(str).str.strip()

  # Filter out products that appear less than 10 times
  item_counts = df_arm['Description'].value_counts()
  frequent_items = item_counts[item_counts >= 10].index
  df_arm_filtered = df_arm[df_arm['Description'].isin(frequent_items)]

  # Create the transaction list format
  arm_transactions = df_arm_filtered.groupby(
      'InvoiceNo')['Description'].apply(list).reset_index()

  # Save
  arm_transactions.to_csv(os.path.join(
      outputPath, 'arm_transactions.csv'), index=False)
  print(
      f"Saved ARM data to {os.path.join(outputPath, 'arm_transactions.csv')}")
