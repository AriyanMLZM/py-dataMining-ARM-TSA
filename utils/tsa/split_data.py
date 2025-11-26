def split_data(dataset, split_ratio=0.8):
  print(f"Total time series length: {len(dataset)} days.")

  split_point = int(len(dataset) * split_ratio)
  train = dataset.iloc[:split_point]
  test = dataset.iloc[split_point:]

  print(f"\nTraining set length: {len(train)} days.")
  print(f"Testing set length: {len(test)} days.")

  return train, test
