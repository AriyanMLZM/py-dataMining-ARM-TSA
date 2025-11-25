import os
from .. import draw_line


def prep_TSA(dataset, output_path):
  draw_line("Preprocessing for Time Series Analysis")

  df_tsa = dataset.set_index('InvoiceDate')

  # Calculate daily total sales
  tsa_daily_sales = df_tsa['TotalAmount'].resample('D').sum().reset_index()
  tsa_daily_sales.columns = ['Date', 'DailySales']
  tsa_daily_sales.to_csv(os.path.join(
      output_path, 'tsa_daily_sales.csv'), index=False)

  print(
      f"Saved TSA data to {os.path.join(output_path, 'tsa_daily_sales.csv')}")
  return tsa_daily_sales
