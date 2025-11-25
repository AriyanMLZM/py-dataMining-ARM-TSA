from utils.preprocessing import detect_missing_values
from utils import load_csv, save_csv, draw_line

# Paths
dataset_path = './dataset/Online Retail.csv'
output_path = './output/cleaned_data.csv'
plots_path = './plots/'


def main():
  # Load dataset
  dataset = load_csv(dataset_path)

  if dataset is not None:
    print('\nFirst 10 rows:')
    print(dataset.head(10))

    # Handle missing values
    detect_missing_values(dataset)


if __name__ == '__main__':
  main()
