import matplotlib.pyplot as PLT
import seaborn as SNS
import os


def eda_ARM(cleaned_df, arm_transactions, output_path):
  # Basket size distribution
  basket_size = cleaned_df.groupby('InvoiceNo')['Description'].nunique()

  PLT.figure(figsize=(8, 6))
  SNS.histplot(basket_size[basket_size <= basket_size.quantile(
      0.99)], bins=30, kde=False, color='darkgreen')
  PLT.title('Distribution of Basket Size (Products per Transaction)')
  PLT.xlabel('Number of Unique Products')
  PLT.ylabel('Number of Transactions (Frequency)')
  PLT.tight_layout()
  PLT.savefig(os.path.join(output_path, 'eda_basket_size_distribution.png'))
  PLT.close()

  # Item frequency: Bar chart of most frequently purchased items (from ARM data)
  top_arm_items = arm_transactions['Description'].explode(
  ).value_counts().head(10)

  PLT.figure(figsize=(10, 6))
  SNS.barplot(x=top_arm_items.values, y=top_arm_items.index,
              palette='cividis', hue=top_arm_items.index)
  PLT.title('Top 10 Most Frequent Items (Filtered for ARM)')
  PLT.xlabel('Total Occurrences in Transactions')
  PLT.ylabel('Product Description')
  PLT.tight_layout()
  PLT.savefig(os.path.join(output_path, 'eda_arm_item_frequency.png'))
  PLT.close()
