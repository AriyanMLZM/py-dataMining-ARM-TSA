import pmdarima as PM
import pandas as PD
from .calculate_metrics import calculate_metrics


def auto_arima(train, test):
  auto_model = PM.auto_arima(
      train['DailySales'],
      start_p=1, start_q=1,
      max_p=3, max_q=3,
      m=7,  # Weekly seasonality
      d=None,  # Let model determine differencing order
      seasonal=True,
      stepwise=True,
      suppress_warnings=True,
      error_action='ignore',
      information_criterion='aic'
  )

  auto_model = PM.auto_arima(
      train['DailySales'],
      start_p=1, start_q=1,
      max_p=3, max_q=3,
      m=7,  # Weekly seasonality
      seasonal=True,
      stepwise=True,
      suppress_warnings=True,
      error_action='ignore',
      information_criterion='aic'
  )

  # Get the Predictions on the Test Set (auto_pred)
  # We set n_periods equal to the length of the test data
  auto_pred = auto_model.predict(n_periods=len(test))
  auto_pred.index = test.index
  # auto_pred is now ready to be passed as the third prediction argument

  # Get the Forecast for Future Values (auto_forecast)
  forecast_steps = 14
  auto_forecast = auto_model.predict(n_periods=forecast_steps)

  # Create a date index for the forecast
  last_date = test.index.max()
  forecast_dates = PD.date_range(
      start=last_date + PD.Timedelta(days=1),
      periods=forecast_steps,
      freq='D'
  )
  auto_forecast.index = forecast_dates

  auto_mae, auto_rmse = calculate_metrics(
      test['DailySales'], auto_pred)

  print(f"Optimal ARIMA Order found: {auto_model.order}")
  print(f"Optimal Seasonal Order found: {auto_model.seasonal_order}")
  print(f"\nmae: {auto_mae.round(2)}")
  print(f"rmse: {auto_rmse.round(2)}")

  return auto_model.order, auto_model.seasonal_order, auto_mae.round(2), auto_rmse.round(2), auto_pred, auto_forecast
