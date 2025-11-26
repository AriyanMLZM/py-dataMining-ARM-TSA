import ast
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


def run_ARM(arm_transactions, min_support, min_confidence):
  transactions = arm_transactions['Description'].apply(
      lambda x: ast.literal_eval(x) if isinstance(x, str) else x).tolist()

  # 1. One-Hot Encoding
  te = TransactionEncoder()
  te_ary = te.fit(transactions).transform(transactions)
  df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

  print(f"One-Hot Encoded DataFrame shape: {df_encoded.shape}")

  # 2. Apply the Apriori algorithm
  frequent_itemsets = apriori(
      df_encoded, min_support=min_support, use_colnames=True)
  print(
      f"Found {len(frequent_itemsets)} frequent itemsets with support >= {min_support}.")

  # 3. Generate association rules
  rules = association_rules(
      frequent_itemsets, metric="confidence", min_threshold=min_confidence)
  print(
      f"Generated {len(rules)} initial rules with confidence >= {min_confidence}.")

  # 5. Filter and Rank rules
  rules_filtered = rules[rules['lift'] > 1].sort_values(
      by='lift', ascending=False)

  # Select the top 10 most interesting rules
  top_10_rules = rules_filtered.head(10).copy()

  # Format Antecedents and Consequents for readability
  top_10_rules['Antecedent'] = top_10_rules['antecedents'].apply(
      lambda x: ', '.join(list(x)))
  top_10_rules['Consequent'] = top_10_rules['consequents'].apply(
      lambda x: ', '.join(list(x)))

  # Select final columns for the presentation table (5.2)
  final_rules_table = top_10_rules[[
      'Antecedent', 'Consequent', 'support', 'confidence', 'lift']].reset_index(drop=True)

  return final_rules_table, rules
