from __future__ import division
__author__ = 'kitty'
import networkx as nx


def discrepency_node(nodedegree_uncertain,nodedegree_certain):
    return abs(nodedegree_uncertain-nodedegree_certain)


def discrepency(node_degree_dict_uncertain,node_degree_dict_certain):
  discrepency=[]
  for each_node_in_g in node_degree_dict_uncertain:
    degree_g=node_degree_dict_uncertain[each_node_in_g]
    degree_gd=node_degree_dict_certain[each_node_in_g]
    discrepency.append(abs(degree_g-degree_gd))
  return discrepency


def vertex_degree(node_degree_dict):
    hist_degree={}
    for d in node_degree_dict.values():
      if d in hist_degree:
        hist_degree[d]+=1
      else:
        hist_degree[d]=1
    return hist_degree


def shortest_path(G):
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
           # print 'SP from %s to %s is %d'%(source_node,target_node,sp)

 #print(shortest_path_count)
 return shortest_path_count


def clustering_co(G,node_degree_dict):
    degree_nodes_dict={}
    for each_node_in_g in node_degree_dict:
        i=node_degree_dict[each_node_in_g]
        if degree_nodes_dict.has_key(i):
            degree_nodes_dict[i].append(each_node_in_g)
        else :
           degree_nodes_dict[i]=[each_node_in_g]
    print("degree nodes dict")
    print(degree_nodes_dict)
    node_clustering_coefficient={}
    #print(nx.clustering(G))
    for each_item in degree_nodes_dict:
     node_clustering_coefficient[each_item]=nx.average_clustering(G,degree_nodes_dict[each_item])
    #print("clustering coefficient are:")
    #print( node_clustering_coefficient)
    return node_clustering_coefficient

def betweeness_centrality(G,node_degree_dict):
    node_betweeness_centrality={}
    betweeness_value=nx.betweenness_centrality(G)
    #print("betweeness values are")
    #print(betweeness_value)
    for each_node_for_betweenness in node_degree_dict:
       i=node_degree_dict[each_node_for_betweenness]
       if node_betweeness_centrality.has_key(i):
         node_betweeness_centrality[i].append(betweeness_value[each_node_for_betweenness])
       else:
         node_betweeness_centrality[i]=[betweeness_value[each_node_for_betweenness]]
    #print(node_betweeness_centrality)
    average_betweeness_centrality={}
    for index_degree in node_betweeness_centrality:
       sum_betweeness_centrality=sum(node_betweeness_centrality[index_degree])
       average_betweeness_centrality[index_degree]=sum_betweeness_centrality/len(node_betweeness_centrality[index_degree])
    #print(average_betweeness_centrality)
    return average_betweeness_centrality






