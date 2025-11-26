import pandas as PD
import os
from utils.tsa import split_data, moving_avg, manual_arima, plot_tsa, auto_arima
from utils.tsa.calculate_metrics import calculate_metrics
from utils import load_csv, draw_line

# Configs
OUTPUT_CLEANED_PATH = './output/cleaned'
TSA_DAILY_SALES_PATH = os.path.join(OUTPUT_CLEANED_PATH, "tsa_daily_sales.csv")
OUTPUT_PLOTS_PATH = './output/plots'

WINDOW_SIZE = 7  # for Moving Average
ARIMA_ORDER = (1, 1, 1)  # for manual Arima


def main():
  # Load dataset created for tsa
  tsa_daily_sales = PD.read_csv(TSA_DAILY_SALES_PATH, parse_dates=['Date'])

  if tsa_daily_sales is not None:
    tsa_daily_sales.set_index('Date', inplace=True)
    tsa_daily_sales = tsa_daily_sales.asfreq('D').fillna(0)

    # Split train test
    draw_line("TSA: Splitting Train-Test")
    train, test = split_data(tsa_daily_sales, 0.8)

    # Moving Avg Model
    draw_line("TSA: Moving AVG Model")
    ma_pred, ma_forecast, ma_mae, ma_rmse = moving_avg(
        train, test, WINDOW_SIZE)

    # Manual Arima Model
    draw_line("TSA: Manual Arima (1, 1, 1)")
    arima_pred, arima_forecast, arima_mae, arima_rmse = manual_arima(
        train, test, ARIMA_ORDER)

    # Auto Arima Model
    draw_line("TSA: Auto Arima (Sarima)")
    auto_order, auto_seasonal_order, auto_mae, auto_rmse, auto_pred, auto_forecast = auto_arima(
        train, test)

    # Create Comparison Table
    draw_line("Model Comparison Table")
    metrics_data = {
        'Model': [
            f'Moving Average ({WINDOW_SIZE} Day)',
            f'Manual ARIMA{ARIMA_ORDER}',
            f'Auto ARIMA{auto_order}x{auto_seasonal_order}'
        ],
        'MAE ($)': [ma_mae, arima_mae, auto_mae],
        'RMSE ($)': [ma_rmse, arima_rmse, auto_rmse]
    }
    comparison_df = PD.DataFrame(metrics_data)
    print(comparison_df.to_string(
        index=False, float_format=lambda x: f'{x:.2f}'))

    # Create Visualizations
    draw_line("Creating TSA Plots")
    os.makedirs(OUTPUT_PLOTS_PATH, exist_ok=True)
    plot_tsa(test, ma_pred, arima_pred,
             auto_pred, ma_forecast, arima_forecast, auto_forecast, tsa_daily_sales, OUTPUT_PLOTS_PATH)

  else:
    print(
        f"\nCan not load {TSA_DAILY_SALES_PATH}\nPlease run main_preprocessing.py first or main.py for whole project.")


if __name__ == '__main__':
  main()
