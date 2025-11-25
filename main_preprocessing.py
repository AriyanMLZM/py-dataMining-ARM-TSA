from utils.preprocessing import detect_missing_values, clean_data, prep_ARM, prep_TSA
from utils import load_csv
import os

# Paths
dataset_path = '.\dataset\online_retail.csv'
output_cleaned_path = '.\output\cleaned'


def main():
  # Load dataset
  dataset = load_csv(dataset_path)

  if dataset is not None:
    print('\nFirst 10 rows:')
    print(dataset.head(10))

    # Clean data
    detect_missing_values(dataset)
    cleaned_data = clean_data(dataset)

    # Preprocessing for ARM and TSA analysis
    os.makedirs(output_cleaned_path, exist_ok=True)
    prep_ARM(cleaned_data, outputPath=output_cleaned_path)
    prep_TSA(cleaned_data, outputPath=output_cleaned_path)


if __name__ == '__main__':
  main()
