import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from main_preprocessing import main as preprocessing


def main():
  print("\n# Preprocessing")
  preprocessing()


if __name__ == '__main__':
  main()


# Config
FILE_PATH = 'online_retail.csv'
PLOTS_DIR = 'output/plots/'
CLEANED_DIR = 'output/cleaned'
sns.set_style("whitegrid")

# Create output directories if they don't exist
os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(CLEANED_DIR, exist_ok=True)
print(f"Created directories: {PLOTS_DIR} and {CLEANED_DIR}")

# =======================================================================
# PART 2: EXPLORATORY DATA ANALYSIS (STEP 4)
# =======================================================================


def perform_eda(cleaned_df, arm_transactions, tsa_daily_sales):
  """
  Performs all requested visualizations and saves them to /output/plots/.
  """
  print("\n--- 3. Performing EDA and Saving Plots ---")

  # --- 4.1 General Dataset Exploration ---

  # 1. Distribution plots: Quantity and UnitPrice
  fig, axes = plt.subplots(1, 2, figsize=(14, 5))
  q_max = cleaned_df['Quantity'].quantile(0.99)
  p_max = cleaned_df['UnitPrice'].quantile(0.99)

  sns.histplot(cleaned_df[cleaned_df['Quantity'] <= q_max]
               ['Quantity'], bins=30, kde=True, ax=axes[0], color='skyblue')
  axes[0].set_title(f'Distribution of Quantity (up to {q_max:.0f})')
  axes[0].set_xlabel('Quantity')
  axes[0].set_ylabel('Frequency')

  sns.histplot(cleaned_df[cleaned_df['UnitPrice'] <= p_max]
               ['UnitPrice'], bins=30, kde=True, ax=axes[1], color='coral')
  axes[1].set_title(f'Distribution of Unit Price (up to ${p_max:.2f})')
  axes[1].set_xlabel('Unit Price ($)')
  axes[1].set_ylabel('Frequency')
  plt.tight_layout()
  plt.savefig(os.path.join(PLOTS_DIR, 'eda_general_distributions.png'))
  plt.close()

  # 2. Top products (by Transaction Count)
  top_n = 15
  top_products = cleaned_df.groupby(
      'Description')['InvoiceNo'].nunique().sort_values(ascending=False).head(top_n)

  plt.figure(figsize=(10, 6))
  sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
  plt.title(
      f'Top {top_n} Most Frequently Purchased Products (by Transaction Count)')
  plt.xlabel('Number of Transactions')
  plt.ylabel('Product Description')
  plt.tight_layout()
  plt.savefig(os.path.join(PLOTS_DIR, 'eda_top_products_transactions.png'))
  plt.close()

  # 3. Geographic distribution: Sales by country (top 10)
  country_sales = cleaned_df.groupby(
      'Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)

  plt.figure(figsize=(10, 6))
  sns.barplot(x=country_sales.index, y=country_sales.values, palette='plasma')
  plt.title('Top 10 Countries by Total Sales')
  plt.xlabel('Country')
  plt.ylabel('Total Sales ($)')
  plt.xticks(rotation=45, ha='right')
  plt.ticklabel_format(style='plain', axis='y')
  plt.tight_layout()
  plt.savefig(os.path.join(PLOTS_DIR, 'eda_country_sales.png'))
  plt.close()

  # --- 4.2 EDA for Association Rules ---

  # 1. Basket size distribution
  basket_size = cleaned_df.groupby('InvoiceNo')['Description'].nunique()

  plt.figure(figsize=(8, 6))
  sns.histplot(basket_size[basket_size <= basket_size.quantile(
      0.99)], bins=30, kde=False, color='darkgreen')
  plt.title('Distribution of Basket Size (Products per Transaction)')
  plt.xlabel('Number of Unique Products')
  plt.ylabel('Number of Transactions (Frequency)')
  plt.tight_layout()
  plt.savefig(os.path.join(PLOTS_DIR, 'eda_basket_size_distribution.png'))
  plt.close()

  # 2. Item frequency: Bar chart of most frequently purchased items (from ARM data)
  top_arm_items = arm_transactions['Description'].explode(
  ).value_counts().head(10)

  plt.figure(figsize=(10, 6))
  sns.barplot(x=top_arm_items.values, y=top_arm_items.index, palette='cividis')
  plt.title('Top 10 Most Frequent Items (Filtered for ARM)')
  plt.xlabel('Total Occurrences in Transactions')
  plt.ylabel('Product Description')
  plt.tight_layout()
  plt.savefig(os.path.join(PLOTS_DIR, 'eda_arm_item_frequency.png'))
  plt.close()

  # --- 4.3 EDA for Time Series ---

  # Time series plot: Line plot showing daily total sales over time
  plt.figure(figsize=(12, 6))
  plt.plot(tsa_daily_sales['Date'], tsa_daily_sales['DailySales'],
           label='Daily Sales', color='tab:blue', alpha=0.6)

  # Moving average: Plot a 7-day moving average
  tsa_daily_sales['7_day_MA'] = tsa_daily_sales['DailySales'].rolling(
      window=7).mean()
  plt.plot(tsa_daily_sales['Date'], tsa_daily_sales['7_day_MA'],
           label='7-Day Moving Average', color='red', linewidth=2)

  plt.title('Daily Total Sales and 7-Day Moving Average Over Time')
  plt.xlabel('Date')
  plt.ylabel('Total Sales ($)')
  plt.legend()
  plt.grid(True, which='both', linestyle='--', linewidth=0.5)
  plt.tight_layout()
  plt.savefig(os.path.join(PLOTS_DIR, 'eda_tsa_daily_sales.png'))
  plt.close()

  print("\nAll EDA plots have been successfully saved to the 'output/plots/' directory.")


# --- MAIN EXECUTION ---
try:
  cleaned_df = load_and_clean_data(FILE_PATH)
  arm_transactions, tsa_daily_sales = prepare_for_analysis(cleaned_df)
  perform_eda(cleaned_df, arm_transactions, tsa_daily_sales)
  print("\nPreprocessing and EDA completed successfully.")

except FileNotFoundError:
  print(
      f"\nError: The file '{FILE_PATH}' was not found. Please ensure it is uploaded.")
except Exception as e:
  print(f"\nAn error occurred during execution: {e}")
