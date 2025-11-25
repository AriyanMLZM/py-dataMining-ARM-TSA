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
