from utils.preprocessing import detect_missing_values, clean_data, prep_ARM, prep_TSA
from utils.eda import eda_ARM, eda_general, eda_TSA
from utils import load_csv, draw_line
import os

# Paths
dataset_path = './dataset/online_retail.csv'
output_cleaned_path = './output/cleaned'
output_plots_path = './output/plots'


def main():
  # Load dataset
  dataset = load_csv(dataset_path)

  if dataset is not None:
    print('\nFirst 10 rows:')
    print(dataset.head(10))

    # Make Output Dirs
    os.makedirs(output_cleaned_path, exist_ok=True)
    os.makedirs(output_plots_path, exist_ok=True)

    # Clean data
    detect_missing_values(dataset)
    cleaned_df = clean_data(dataset, output_path=output_cleaned_path)

    # Preprocessing for ARM and TSA analysis
    arm_transactions = prep_ARM(cleaned_df, output_path=output_cleaned_path)
    tsa_daily_sales = prep_TSA(cleaned_df, output_path=output_cleaned_path)

    # EDA
    draw_line("EDA - Plotting")
    eda_general(cleaned_df, output_path=output_plots_path)
    eda_ARM(cleaned_df, arm_transactions, output_path=output_plots_path)
    eda_TSA(tsa_daily_sales, output_path=output_plots_path)
    print(f"All plots saved to {output_plots_path} dir.")


if __name__ == '__main__':
  main()
