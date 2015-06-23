#!/usr/bin/python
#coding=utf-8
'''
Created on Apr 28, 2015

@author: kitty
'''
import networkx as nx #这是猫的代码
import matplotlib.pyplot as plt
import numpy as np
import os



G=nx.Graph()
G.add_node('isolated_node')
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
# G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(4, 3)
G.add_edge(4, 5)


Gd=nx.Graph()
Gd.add_node('isolated_node')
Gd.add_node(1)
Gd.add_node(2)
Gd.add_node(3)
Gd.add_node(4)
Gd.add_node(5)
Gd.add_edge(1, 2)
Gd.add_edge(1, 3)
# G.add_edge(1, 5)
Gd.add_edge(2, 3)

Gd.add_edge(4, 5)





print(nx.degree(G))


degree_sequence=list(nx.degree(G).values())
print("Degree sequence %s" % degree_sequence)
hist_degree={}
for d in degree_sequence:
    if d in hist_degree:
        hist_degree[d]+=1
    else:
        hist_degree[d]=1
print("degree #nodes")
for d in hist_degree:
    print('%d %d' % (d,hist_degree[d]))



#draw the pictures of the vertice degree
plt.figure(1)
#plt.plot(np.array(x_degree),np.array(y_degree))

#plt.plot(x_degree,y_degree)
plt.plot(hist_degree.keys(),hist_degree.values())

nx.set_node_attributes(G, 'degree', nx.degree(G))
nx.set_node_attributes(Gd, 'degree', nx.degree(Gd))

#print G.nodes (True)
#print G.nodes ()
node_degree={}

for each_node_in_g, node_atrribute_dict in G.nodes (True):
    i=node_atrribute_dict['degree']
    if i in node_degree:
        node_degree[i].append(each_node_in_g)
    else :
        node_degree[i]=[each_node_in_g]

for each_node_in_g, node_atrribute_dict in G.nodes (True):
    i=node_atrribute_dict['degree']
    if i in node_degree:
        node_degree[i].append(each_node_in_g)
    else :
        node_degree[i]=[each_node_in_g]

def median_of_list(lst):
    if not lst:
        return
    lst=sorted(lst)
    if len(lst)%2==1:
        return lst[len(lst)//2]
    else:
        return (lst[len(lst)//2-1]+lst[len(lst)//2])/2.0
def first_quater_of_list(lst):
    if not lst:
        return
    lst=sorted(lst)
    mid=len(lst)//2


discrepency=[]
for each_node_in_g, node_atrribute_dictd in G.nodes (True):
    degree_g=node_atrribute_dict['degree']
    degree_gd=Gd.node[each_node_in_g]['degree']
    discrepency.append(abs(degree_g-degree_gd))

#discrepency=sorted(discrepency)
dis_length=len(discrepency)
dis_median=median_of_list(discrepency)
#dis_upper=discrepency[int(len(discrepency)*0.96)-1]
print(discrepency)
dis_array=np.array(discrepency)

plt.figure(2)

plt.boxplot(dis_array)



#print(node_degree)


for a_node in G.nodes():
    print a_node, G.node[a_node]['degree']

#nodes_list = G.nodes()
#for index,a_node in enumerate(nodes_list):
#    print nodes_list[index], G.node[nodes_list[index]]['degree']




all_nodes=G.nodes()
print("shortest path")
shortest_path_count= {1:0}
for index, source_node in enumerate (all_nodes):
    for target_node in all_nodes[index+1:]:
        try:
            sp=nx.shortest_path_length(G,source=source_node,target=target_node)
        except nx.NetworkXNoPath, e:
            print 'NO Path from %s to %s'%(source_node,target_node)
        else:
            if sp in shortest_path_count : shortest_path_count[sp]+=1
            else : shortest_path_count[sp]=1
            print 'SP from %s to %s is %d'%(source_node,target_node,sp)
print 'SP statistics: %s'%(shortest_path_count)

plt.figure(5)
#plt.plot(np.array(x_degree),np.array(y_degree))

#plt.plot(x_degree,y_degree)
plt.plot(shortest_path_count.keys(),shortest_path_count.values())
# print(nx.shortest_path(G))
# print(nx.shortest_path_length(G))
# shortest_path_sequence=nx.shortest_path_length(G).values()
# hist_sp={}
# print(("Shortest path sequence %s" % shortest_path_sequence)
# for eachitem in shortest_path_sequence:
#     for i in eachitem:
#         print('%d %d' % (i,eachitem[i]))



print("clustering coefficient")
node_clustering_coefficient={}
for each_item in node_degree:
    node_clustering_coefficient[each_item]=nx.average_clustering(G,node_degree[each_item])
print(node_clustering_coefficient)
print(nx.clustering(G))

print("betweenness_centrality")
node_betweeness_centrality={}
betweeness_value=nx.betweenness_centrality(G)
for each_node_for_betweenness, node_atrribute_for_betweeness in G.nodes (True):
    i=node_atrribute_for_betweeness['degree']
    if i in node_betweeness_centrality:
        node_betweeness_centrality[i].append(betweeness_value[each_node_for_betweenness])
    else:
        node_betweeness_centrality[i]=[betweeness_value[each_node_for_betweenness]]

average_betweeness_centrality={}
for index_degree in node_betweeness_centrality:
    sum_betweeness_centrality=0
    for each_value in node_betweeness_centrality[index_degree]:
        sum_betweeness_centrality+=each_value
    average_betweeness_centrality[index_degree]=sum_betweeness_centrality/len(node_betweeness_centrality[index_degree])
print(average_betweeness_centrality)


#  print(nx.betweenness_centrality(G))
#
pos=nx.spring_layout(G) # positions for all nodes

# nodes
plt.figure(3)
nx.draw_networkx_nodes(G,pos,noG=700)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.figure(4)
nx.draw_networkx_nodes(Gd,pos,noG=700)
nx.draw_networkx_edges(Gd,pos)
nx.draw_networkx_labels(Gd,pos,font_size=20,font_family='sans-serif')

# nx.draw(G)
# G=nx.cubical_graph()
#nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')
#plt.xlim(-0.05,1.05)
#plt.ylim(-0.05,1.05)
#plt.axis('off')
 #plt.savefig('random_geometric_graph.png')

plt.show()