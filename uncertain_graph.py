from __future__ import division
__author__ = 'kitty'
#!/usr/bin/python
#coding=utf-8

'''
Created on Apr 28, 2015

@author: kitty
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import org.fri.kitty.mpdef as mpdef
import org.fri.kitty.draw_graph_basic as dg
import org.fri.kitty.measure_def as mf
import org.fri.kitty.draw_measure as dm
#G=nx.gnp_random_graph(1000,0.1)


'''

G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
edge_pro_dict_gp={}
edge_pro_dict_gp[(1,2)]=0.52
edge_pro_dict_gp[(2,3)]=0.51
edge_pro_dict_gp[(3,4)]=0.50


edge_pro_dict={}
for each_edge in G.edges():
    i=round(np.random.random(),2)
    while(i==0.0):
        i=round(np.random.random(),2)
    edge_pro_dict[each_edge]=i


print(edge_pro_dict)
'''

G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(2,5)
G.add_edge(2,7)
G.add_edge(2,9)
G.add_edge(3,4)
G.add_edge(3,6)
G.add_edge(3,7)
G.add_edge(3,8)
G.add_edge(8,7)
edge_pro_dict_adr={}
edge_pro_dict_adr[(1,2)]=0.4
edge_pro_dict_adr[(2,3)]=1
edge_pro_dict_adr[(2,5)]=0.45
edge_pro_dict_adr[(2,7)]=0.3
edge_pro_dict_adr[(2,9)]=0.45
edge_pro_dict_adr[(3,4)]=0.3
edge_pro_dict_adr[(3,6)]=0.3
edge_pro_dict_adr[(3,7)]=0.2
edge_pro_dict_adr[(3,8)]=0.1
edge_pro_dict_adr[(7,8)]=0.9



#nx.set_edge_attributes(G, 'probability', edge_pro_dict)
#nx.set_edge_attributes(G, 'probability', edge_pro_dict_gp)
nx.set_edge_attributes(G, 'probability', edge_pro_dict_adr)
#print(G.edges(data=True))
node_degree_dict={}
for each_node in G.nodes():
   node_degree_dict[each_node]=0.0
   for each_edge_index in edge_pro_dict_adr:
       if each_node in each_edge_index:
           node_degree_dict[each_node] += edge_pro_dict_adr[each_edge_index]

#print(node_degree_dict)


Gmp=mpdef.mp(G)

Ggp=mpdef.gp(G,edge_pro_dict_adr, node_degree_dict)

Gadr=mpdef.adr(G,edge_pro_dict_adr, node_degree_dict,40)

Gabm=mpdef.abm(G,edge_pro_dict_adr, node_degree_dict)

node_degree_dict_mp=nx.degree(Gmp)
#print(node_degree_dict_mp)

# discrepency caculator
discrepency_mp=mf.discrepency(node_degree_dict,node_degree_dict_mp)
#print discrepency_mp

'''
#vertex degrees caculator
vertex_degree_mp=mf.vertex_degree(node_degree_dict_mp)



# shortest path caculator
shortest_path_mp=mf.shortest_path(Gmp)

#clustering coefficient
clustering_co_mp=mf.clustering_co(Gmp,node_degree_dict_mp)
#print("clustering coefficient")
#print(clustering_co_mp)


#betweeness centrality
betweeness_centrality_mp=mf.betweeness_centrality(Gmp,node_degree_dict_mp)



#

dm.plot_discrepency(discrepency_mp)
dm.plot_vertex_degree(vertex_degree_mp)
dm.plot_shortest_path(shortest_path_mp)
dm.plot_clustering_co(clustering_co_mp)
dm.plot_betweeness_centrality(betweeness_centrality_mp)


'''
dg.draw_graphs(G,edge_pro_dict_adr,Gmp,Ggp,Gadr,Gabm)
#node_degree_dict_gp=nx.degree(Ggp)
#print(node_degree_dict_gp)

# discrepency caculator
#discrepency_gp=mf.discrepency(node_degree_dict,node_degree_dict_gp)
#print discrepency_gp