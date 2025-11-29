import os
import pandas as PD
import networkx as NX
import plotly.graph_objects as GO


def main():
  # load top arm rules
  top_rules = PD.read_csv(os.path.join(
      './output', 'top_arm_rules.csv'))

  if top_rules is not None:
    G = NX.DiGraph()

    for _, row in top_rules.iterrows():
      ant = row["Antecedent"]
      con = row["Consequent"]

      G.add_edge(
          ant, con,
          support=row["support"],
          confidence=row["confidence"],
          lift=row["lift"]
      )

    pos = NX.spring_layout(G, seed=42)

    fig = GO.Figure()

    arrow_annotations = []
    for u, v, d in G.edges(data=True):
      x0, y0 = pos[u]
      x1, y1 = pos[v]

      arrow_annotations.append(
          dict(
              ax=x0, ay=y0,
              x=x1, y=y1,
              xref="x", yref="y",
              axref="x", ayref="y",
              showarrow=True,
              arrowhead=3,
              arrowsize=1.5,
              arrowwidth=1.5,
              opacity=0.8
          )
      )

    for u, v, d in G.edges(data=True):
      x0, y0 = pos[u]
      x1, y1 = pos[v]

      fig.add_trace(GO.Scatter(
          x=[(x0+x1)/2],
          y=[(y0+y1)/2],
          mode="markers",
          marker=dict(size=20, opacity=0),
          hovertemplate=(
              f"<b>{u}</b> → <b>{v}</b><br><br>"
              f"Confidence: {d['confidence']:.3f}<br>"
              f"Lift: {d['lift']:.2f}<br>"
              f"Support: {d['support']:.3f}<extra></extra>"
          )
      ))

    fig.add_trace(GO.Scatter(
        x=[pos[n][0] for n in G.nodes()],
        y=[pos[n][1] for n in G.nodes()],
        mode="markers+text",
        text=list(G.nodes()),
        textposition="bottom center",
        hoverinfo="text",
        marker=dict(size=40, color="lightgreen", line=dict(width=1))
    ))

    fig.update_layout(
        title="Interactive Association Rules Network (Itemset-Level, Correct Arrows + Hover)",
        annotations=arrow_annotations,
        showlegend=False,
        width=1200,
        height=800,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    fig.show()

  else:
    print("\n Please run main_ARM.py first to generate top_arm_rules.csv.")


if __name__ == "__main__":
  main()
