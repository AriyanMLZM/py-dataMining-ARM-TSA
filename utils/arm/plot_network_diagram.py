import networkx as NX
import matplotlib.pyplot as plt
import os


def plot_network_diagram(rules_df, output_path):
  # Create a Directed Graph object
  G = NX.DiGraph()

  # Add edges and nodes based on the top rules
  # Use Lift as the weight to determine the thickness/strength of the connection
  for _, row in rules_df.iterrows():
    # Get the first item from the antecedent/consequent for simpler visualization
    # In a multi-item set, we use the full set name for the node
    ant = row['Antecedent']
    con = row['Consequent']
    lift = row['lift']

    # Add edge with weight = Lift
    G.add_edge(ant, con, weight=lift)

  # Define node and edge aesthetics based on metrics

  # Node sizing by degree (number of connected rules)
  node_sizes = [G.degree(node) * 1000 for node in G]

  # Edge thickness by Lift
  edge_widths = [G[u][v]['weight'] / 5 for u, v in G.edges()]

  # Draw the graph
  plt.figure(figsize=(14, 10))

  # Use spring layout for better node separation
  pos = NX.spring_layout(G, k=0.8, iterations=50)

  # Draw nodes
  NX.draw_networkx_nodes(G, pos, node_size=node_sizes,
                         node_color='skyblue', alpha=0.9)

  # Draw edges (arrows)
  NX.draw_networkx_edges(G, pos, width=edge_widths, edge_color='gray',
                         alpha=0.6, arrowsize=20)

  # Draw labels (product names)
  NX.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

  plt.title(
      "Network Diagram of Top Association Rules", fontsize=16)
  plt.axis('off')

  plot_file = os.path.join(output_path, 'arm_network_diagram.png')
  plt.savefig(plot_file)
  plt.close()
  print(f"Saved Network Diagram to: {plot_file}")
