from __future__ import division
__author__ = 'kitty'

import matplotlib.pyplot as plt
import numpy as np

def plot_discrepency(dis):
 plt.figure()
 plt.boxplot(dis)
 plt.title("distribution of discrepancy per node")
 plt.ylabel("Discrepancy")
 plt.xlabel("mp")
 plt.axes()
 plt.show()


def plot_vertex_degree(vertex_degree):
 plt.figure()
 degree_sum=sum(vertex_degree.values())
 for i in vertex_degree:
     vertex_degree[i]=vertex_degree[i]/degree_sum
 x=range(0,max(vertex_degree.keys())+1)
 for i in x:
     if not vertex_degree.has_key(i):
         vertex_degree[i]=0.0
 plt.plot(x,vertex_degree.values(),color='blue', linestyle='dashed', marker='x')
 plt.title("vertex degree" )
 plt.xticks(range(min(x),max(x),5))
 plt.xlabel("degree")
 plt.ylabel("% of vertices")
 plt.show()


def plot_shortest_path(shortest_path):
    plt.figure()
    shortest_path_sum=sum(shortest_path.values())
    for i in shortest_path:
        shortest_path[i]=shortest_path[i]/shortest_path_sum
    x=range(0,max(shortest_path.keys())+1)
    for i in x:
     if not shortest_path.has_key(i):
        shortest_path[i]=0.0
    plt.plot(x,shortest_path.values(),color='blue', linestyle='dashed', marker='x')
    plt.xticks(x)
    plt.xlabel("SP distance")
    plt.ylabel("% of vertex paris")
    plt.title("shortest path distance")
    plt.show()

def plot_clustering_co(clustering_co):
    plt.figure()
    x=range(0,max(clustering_co.keys())+1)
    for i in x:
     if not clustering_co.has_key(i):
         clustering_co[i]=0.0
    plt.plot(x,clustering_co.values(),color='blue', linestyle='dashed', marker='x')
    plt.xticks(range(min(x),max(x),5))
    plt.title("clustering coefficient")
    plt.xlabel("degree")
    plt.ylabel("clustering coefficient")
    plt.show()


def plot_betweeness_centrality(betweeness_centrality):
    plt.figure()
    x=range(0,max(betweeness_centrality.keys())+1)
    for i in x:
     if not betweeness_centrality.has_key(i):
         betweeness_centrality[i]=0.0
    plt.plot(x,betweeness_centrality.values(),color='blue', linestyle='dashed', marker='x')
    plt.xticks(range(min(x),max(x),5))
    plt.title("betweenness centrality")
    plt.xlabel("degree")
    plt.ylabel("nomalized betweenness")
    plt.show()

