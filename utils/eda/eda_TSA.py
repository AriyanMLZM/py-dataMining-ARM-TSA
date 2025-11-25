import matplotlib.pyplot as PLT
import os


def eda_TSA(tsa_daily_sales, output_path):
  # Time series plot: Line plot showing daily total sales over time
  PLT.figure(figsize=(12, 6))
  PLT.plot(tsa_daily_sales['Date'], tsa_daily_sales['DailySales'],
           label='Daily Sales', color='tab:blue', alpha=0.6)

  # Moving average: Plot a 7-day moving average
  tsa_daily_sales['7_day_MA'] = tsa_daily_sales['DailySales'].rolling(
      window=7).mean()
  PLT.plot(tsa_daily_sales['Date'], tsa_daily_sales['7_day_MA'],
           label='7-Day Moving Average', color='red', linewidth=2)

  PLT.title('Daily Total Sales and 7-Day Moving Average Over Time')
  PLT.xlabel('Date')
  PLT.ylabel('Total Sales ($)')
  PLT.legend()
  PLT.grid(True, which='both', linestyle='--', linewidth=0.5)
  PLT.tight_layout()
  PLT.savefig(os.path.join(output_path, 'eda_tsa_daily_sales.png'))
  PLT.close()
