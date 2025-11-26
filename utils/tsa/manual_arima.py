import pandas as PD
from statsmodels.tsa.arima.model import ARIMA
from .calculate_metrics import calculate_metrics


def manual_arima(train, test, order):
  # Fit model on Training Data
  model = ARIMA(train['DailySales'], order=order)
  model_fit = model.fit()
  print(f"ARIMA({order}) Model Summary:")
  print(model_fit.summary().tables[1].as_text())  # Print parameter table

  # Prediction on Test Set
  start_index = test.index.min()
  end_index = test.index.max()

  arima_predictions = model_fit.predict(
      start=start_index, end=end_index, dynamic=False)

  # Calculate metrics
  mae, rmse = calculate_metrics(test['DailySales'], arima_predictions)
  print(f"\nmae: {mae.round(2)}")
  print(f"rmse: {rmse.round(2)}")

  # 14-Day Forecast
  forecast_dates = PD.date_range(
      start=test.index[-1] + PD.Timedelta(days=1), periods=14, freq='D')
  arima_forecast = model_fit.forecast(steps=14)
  arima_forecast.index = forecast_dates

  return arima_predictions, arima_forecast, mae, rmse
