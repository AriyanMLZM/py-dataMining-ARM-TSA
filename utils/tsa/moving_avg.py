import pandas as PD
from .calculate_metrics import calculate_metrics


def moving_avg(train, test, window):
  full_series = PD.concat([train, test])

  # Calculate rolling MA based on training data and subsequent test data
  rolling_mean = full_series['DailySales'].shift(
      1).rolling(window=window).mean()

  # Get predictions for the test set period
  ma_predictions = rolling_mean[test.index]

  # Drop NaNs that occur due to the rolling window calculation
  test_aligned = test['DailySales'].dropna()
  ma_predictions = ma_predictions.loc[test_aligned.index].bfill().fillna(
      0)  # Backfill initial NaNs

  # Calculate metrics
  mae, rmse = calculate_metrics(test_aligned, ma_predictions)
  print(f"mae: {mae.round(2)}")
  print(f"rmse: {rmse.round(2)}")

  # 2. 14-Day Forecast: Forecast based on the last 'window' days of the full training set
  last_train_values = train['DailySales'].tail(window)
  ma_forecast_value = last_train_values.mean()

  forecast_dates = PD.date_range(
      start=test.index[-1] + PD.Timedelta(days=1), periods=14, freq='D')
  ma_forecast = PD.Series(ma_forecast_value, index=forecast_dates)

  return ma_predictions, ma_forecast, mae, rmse
