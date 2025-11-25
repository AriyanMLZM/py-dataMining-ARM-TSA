import pandas as PD
from .draw_line import draw_line


def load_csv(datasetPath):
  draw_line("Loading Dataset")
  try:
    dataset = PD.read_csv(datasetPath)
    print(f"{dataset.shape[0]} rows and {dataset.shape[1]} columns loaded")
    return dataset
  except:
    print("Error Loading Dataset")
    return None


def save_csv(dataset, datasetPath):
  draw_line("Saving New Dataset")
  try:
    dataset.to_csv(datasetPath, index=False)
    print(f"New Data saved in {datasetPath}")
  except:
    print("Error Saving New Dataset")
    return None
