from utils.preprocessing import detect_missing_values, clean_data, prep_ARM, prep_TSA
from utils.eda import eda_ARM, eda_general, eda_TSA
from utils import load_csv, draw_line
import os

# Configs
DATASET_PATH = './dataset/online_retail.csv'
OUTPUT_CLEANED_PATH = './output/cleaned'
OUTPUT_PLOTS_PATH = './output/plots'


def main():
  # Load dataset
  dataset = load_csv(DATASET_PATH)

  if dataset is not None:
    print('\nFirst 10 rows:')
    print(dataset.head(10))

    # Make Output Dirs
    os.makedirs(OUTPUT_CLEANED_PATH, exist_ok=True)
    os.makedirs(OUTPUT_PLOTS_PATH, exist_ok=True)

    # Clean data
    detect_missing_values(dataset)
    cleaned_df = clean_data(dataset, output_path=OUTPUT_CLEANED_PATH)

    # Preprocessing for ARM and TSA analysis
    arm_transactions = prep_ARM(cleaned_df, output_path=OUTPUT_CLEANED_PATH)
    tsa_daily_sales = prep_TSA(cleaned_df, output_path=OUTPUT_CLEANED_PATH)

    # EDA
    draw_line("EDA - Plotting")
    eda_general(cleaned_df, output_path=OUTPUT_PLOTS_PATH)
    eda_ARM(cleaned_df, arm_transactions, output_path=OUTPUT_PLOTS_PATH)
    eda_TSA(tsa_daily_sales, output_path=OUTPUT_PLOTS_PATH)
    print(f"All plots saved to {OUTPUT_PLOTS_PATH} dir.")


if __name__ == '__main__':
  main()
