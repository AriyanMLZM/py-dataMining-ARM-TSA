import matplotlib.pyplot as PLT
import seaborn as SNS
import os


def eda_general(cleaned_df, output_path):
  # Distribution plots: Quantity and UnitPrice
  fig, axes = PLT.subplots(1, 2, figsize=(14, 5))
  q_max = cleaned_df['Quantity'].quantile(0.99)
  p_max = cleaned_df['UnitPrice'].quantile(0.99)

  SNS.histplot(cleaned_df[cleaned_df['Quantity'] <= q_max]
               ['Quantity'], bins=30, kde=True, ax=axes[0], color='skyblue')
  axes[0].set_title(f'Distribution of Quantity (up to {q_max:.0f})')
  axes[0].set_xlabel('Quantity')
  axes[0].set_ylabel('Frequency')

  SNS.histplot(cleaned_df[cleaned_df['UnitPrice'] <= p_max]
               ['UnitPrice'], bins=30, kde=True, ax=axes[1], color='coral')
  axes[1].set_title(f'Distribution of Unit Price (up to ${p_max:.2f})')
  axes[1].set_xlabel('Unit Price ($)')
  axes[1].set_ylabel('Frequency')
  PLT.tight_layout()
  PLT.savefig(os.path.join(output_path, 'eda_general_distributions.png'))
  PLT.close()

  # Top products (by Transaction Count)
  top_n = 15
  top_products = cleaned_df.groupby(
      'Description')['InvoiceNo'].nunique().sort_values(ascending=False).head(top_n)

  PLT.figure(figsize=(10, 6))
  SNS.barplot(x=top_products.values, y=top_products.index,
              palette='viridis', hue=top_products.index)
  PLT.title(
      f'Top {top_n} Most Frequently Purchased Products (by Transaction Count)')
  PLT.xlabel('Number of Transactions')
  PLT.ylabel('Product Description')
  PLT.tight_layout()
  PLT.savefig(os.path.join(output_path, 'eda_top_products_transactions.png'))
  PLT.close()

  # Geographic distribution: Sales by country (top 10)
  country_sales = cleaned_df.groupby(
      'Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)

  PLT.figure(figsize=(10, 6))
  SNS.barplot(x=country_sales.index, y=country_sales.values,
              palette='plasma', hue=country_sales.index)
  PLT.title('Top 10 Countries by Total Sales')
  PLT.xlabel('Country')
  PLT.ylabel('Total Sales ($)')
  PLT.xticks(rotation=45, ha='right')
  PLT.ticklabel_format(style='plain', axis='y')
  PLT.tight_layout()
  PLT.savefig(os.path.join(output_path, 'eda_country_sales.png'))
  PLT.close()
