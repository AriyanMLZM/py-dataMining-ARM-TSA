import os
from utils.arm import run_ARM, plot_rules, plot_network_diagram
from utils import load_csv, draw_line

# Configs
OUTPUT_CLEANED_PATH = './output/cleaned'
TRANSACTIONS_PATH = os.path.join(OUTPUT_CLEANED_PATH, "arm_transactions.csv")
OUTPUT_PLOTS_PATH = './output/plots'
MIN_SUPPORT = 0.01
MIN_CONFIDENCE = 0.3


def main():
  # Load dataset created for arm
  arm_transactions = load_csv(TRANSACTIONS_PATH)

  if arm_transactions is not None:
    draw_line("Association Rule Mining")
    final_rules_table, all_rules = run_ARM(
        arm_transactions, MIN_SUPPORT, MIN_CONFIDENCE)

    print("Top 10 association rules (lift > 1, sorted by lift)")
    print(final_rules_table.to_string(
        index=False, float_format=lambda x: f'{x:.3f}'))
    final_rules_table.to_csv(os.path.join(
        './output', 'top_arm_rules.csv'), index=False)
    print(
        f"\nSaved top association rules to {os.path.join('./output', 'top_arm_rules.csv')}")

    os.makedirs(OUTPUT_PLOTS_PATH, exist_ok=True)
    plot_rules(all_rules, OUTPUT_PLOTS_PATH)
    plot_network_diagram(final_rules_table, OUTPUT_PLOTS_PATH)

  else:
    print("\n Please run main_preprocessing.py first or main.py for whole project.")


if __name__ == '__main__':
  main()
