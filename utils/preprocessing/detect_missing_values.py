import pandas as PD
from .. import draw_line


def detect_missing_values(dataset):
  draw_line("Detecting Missing Values")

  missing_values = dataset.isnull().sum()
  missing_percentage = ((missing_values / len(dataset)) * 100).round(2)

  missing_info = PD.DataFrame({
      'Missing Count': missing_values,
      'Missing Percentage': missing_percentage
  })

  print(missing_info[missing_info['Missing Count'] > 0])

  if missing_values.sum() == 0:
    print("No missing values found!")
  else:
    print(f"\nTotal missing values: {missing_values.sum()}")

  return missing_values
