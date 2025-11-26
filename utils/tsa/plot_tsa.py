import matplotlib.pyplot as plt
import os


def plot_tsa(test, ma_pred, arima_pred, auto_pred, ma_forecast, arima_forecast, auto_forecast, full_df, output_path):
  # --- Plot 1: Actual vs. Predicted Sales on Test Data ---
  plt.figure(figsize=(14, 6))
  plt.plot(test.index, test['DailySales'],
           label='Actual Sales', color='blue', alpha=0.7)
  plt.plot(test.index, ma_pred, label='MA (7 Day) Prediction',
           color='orange', linestyle='--')
  plt.plot(test.index, arima_pred,
           label='Simple ARIMA(1,1,1) Prediction', color='red', linestyle=':')
  plt.plot(test.index, auto_pred, label='Optimal SARIMA Prediction',
           color='green', linestyle='-.', alpha=0.8)

  plt.title('Actual vs. Predicted Daily Sales (Test Set)', fontsize=14)
  plt.xlabel('Date')
  plt.ylabel('Daily Sales ($)')
  plt.legend()
  plt.grid(True, which='both', linestyle='--', linewidth=0.5)

  plot_file_1 = os.path.join(
      output_path, 'tsa_actual_vs_predicted_comparison_all.png')
  plt.savefig(plot_file_1)
  plt.close()
  print(f"Saved plot: {plot_file_1}")

  # --- Plot 2: Forecast plot showing predictions for next 14 days ---
  plt.figure(figsize=(14, 6))

  # Plot historical data (last few months)
  plot_series = full_df['DailySales'].tail(len(test) + 90)
  plt.plot(plot_series.index, plot_series.values,
           label='Historical Sales', color='blue', alpha=0.6)

  # Plot 14-day forecasts
  plt.plot(ma_forecast.index, ma_forecast.values,
           label='MA (7 Day) Forecast', color='orange', linestyle='--')
  plt.plot(arima_forecast.index, arima_forecast.values,
           label='Simple ARIMA(1,1,1) Forecast', color='red', linestyle=':')
  plt.plot(auto_forecast.index, auto_forecast.values,
           label='Optimal SARIMA Forecast', color='green', linestyle='-.', alpha=0.8)

  # Highlight the test period
  plt.axvspan(test.index.min(), test.index.max(),
              color='grey', alpha=0.1, label='Test Period')

  plt.title('14-Day Sales Forecast Comparison', fontsize=14)
  plt.xlabel('Date')
  plt.ylabel('Daily Sales ($)')
  plt.legend()
  plt.grid(True, which='both', linestyle='--', linewidth=0.5)

  plot_file_2 = os.path.join(
      output_path, 'tsa_14_day_forecast_comparison_all.png')
  plt.savefig(plot_file_2)
  plt.close()
  print(f"Saved plot: {plot_file_2}")
