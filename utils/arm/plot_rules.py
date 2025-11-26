import matplotlib.pyplot as PLT
import seaborn as SNS
import os


def plot_rules(rules, output_path):
  PLT.figure(figsize=(10, 6))

  # Scatter plot: support vs. confidence (colored by lift)
  SNS.scatterplot(x="support", y="confidence", size="lift", hue="lift", data=rules,
                  alpha=0.6, sizes=(50, 300), palette='viridis')

  PLT.title(
      'Association Rules: Support vs. Confidence (Colored by Lift)', fontsize=12)
  PLT.xlabel('Support', fontsize=10)
  PLT.ylabel('Confidence', fontsize=10)
  PLT.legend(title='Lift', bbox_to_anchor=(1.05, 1), loc='upper left')
  PLT.grid(True, which='both', linestyle='--', linewidth=0.5)
  PLT.tight_layout()

  plot_file = os.path.join(output_path, 'arm_support_vs_confidence.png')
  PLT.savefig(plot_file)
  PLT.close()
  print(f"\n Saved ARM visualization to: {plot_file}")
