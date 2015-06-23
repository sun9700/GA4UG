__author__ = 'kitty'
import matplotlib.pyplot as plt

import networkx as nx
def draw_graphs(G,edge_pro_dict,Gmp,Ggp,Gadr,Gabm):
  plt.figure(1)
  pos=nx.spring_layout(G) # positions for all nodes
  nx.draw_networkx_nodes(G,pos,noG=800)
  nx.draw_networkx_edges(G,pos)
  nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
  nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_pro_dict)

  plt.figure(2)
  nx.draw_networkx_nodes(Gmp,pos,noG=800)
  nx.draw_networkx_edges(Gmp,pos)
  nx.draw_networkx_labels(Gmp,pos,font_size=10,font_family='sans-serif')

  plt.figure(3)
  nx.draw_networkx_nodes(Ggp,pos,noG=800)
  nx.draw_networkx_edges(Ggp,pos)
  nx.draw_networkx_labels(Ggp,pos,font_size=10,font_family='sans-serif')

  plt.figure(4)
  nx.draw_networkx_nodes(Gadr,pos,noG=800)
  nx.draw_networkx_edges(Gadr,pos)
  nx.draw_networkx_labels(Gadr,pos,font_size=10,font_family='sans-serif')

  plt.figure(5)
  nx.draw_networkx_nodes(Gabm,pos,noG=800)
  nx.draw_networkx_edges(Gabm,pos)
  nx.draw_networkx_labels(Gabm,pos,font_size=10,font_family='sans-serif')

  plt.show()


