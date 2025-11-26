import numpy as NP


def calculate_metrics(y_true, y_pred):
  n = len(y_true)
  y_true, y_pred = NP.array(y_true), NP.array(y_pred)

  # Mean Absolute Error (MAE)
  mae = NP.mean(NP.abs(y_true - y_pred))

  # Root Mean Squared Error (RMSE)
  rmse = NP.sqrt(NP.mean((y_true - y_pred)**2))

  return mae, rmse
