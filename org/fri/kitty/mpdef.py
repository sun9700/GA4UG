import networkx as nx
import numpy as np
from random import choice


def mp(G):

    Gmp=nx.Graph()
    for each_node in G.nodes():
        Gmp.add_node(each_node)
    for each_edge_source,each_edge_des,edge_atrribute_dict in G.edges(data=True):
        if edge_atrribute_dict['probability']>=0.5:
            Gmp.add_edge(each_edge_source,each_edge_des)


    return Gmp


def gp(G,edge_pro_dict,node_degree_dict):

    Ggp=nx.Graph()

    for each_node in G.nodes():
        Ggp.add_node(each_node)
    edge_pro_order=sorted(edge_pro_dict.iteritems(), key=lambda d:d[1],reverse=True)
    for each_edge_order in edge_pro_order:
        u=each_edge_order[0][0]
        v=each_edge_order[0][1]
        discrepency_u=nx.degree(Ggp)[u]-node_degree_dict[u]
        discrepency_v=nx.degree(Ggp)[v]-node_degree_dict[v]
        if(abs(discrepency_u+1)+abs(discrepency_v+1)<abs(discrepency_u)+abs(discrepency_v)):
            Ggp.add_edge(u,v)
    return Ggp



def adr(G,edge_pro_dict,node_degree_dict,swap=0):
    Gadr=nx.Graph()
    sum_p=int(round(sum(edge_pro_dict.values())))
    #print("expected time is")
    #print (sum_p)
    for each_node in G.nodes():
        Gadr.add_node(each_node)
    edge_pro_order=sorted(edge_pro_dict.iteritems(), key=lambda d:d[1],reverse=True)

    edge_count=0
    for each_edge_order in edge_pro_order:
       print (each_edge_order)
       if edge_count>=sum_p:
           break
       i=np.random.random()
       print("the random value is ")
       print (i)
       if i <= each_edge_order[1]:
           Gadr.add_edge(each_edge_order[0][0],each_edge_order[0][1])
           edge_count=edge_count+1
           print("add edge")
           print(each_edge_order[0])

    left_edges=[]
    for each_left_edge in edge_pro_order:
        left_edges.append(each_left_edge[0])

    for each_edge_adr in Gadr.edges():
         left_edges.remove(each_edge_adr)
    #print(left_edges)

    for s in range(swap):
        print("swap time s")
        print(s)
        e1=choice(Gadr.edges())
        u=e1[0]
        v=e1[1]
        discrepency_u=nx.degree(Gadr)[u]-node_degree_dict[u]
        discrepency_v=nx.degree(Gadr)[v]-node_degree_dict[v]
        print(u)
        print(v)
        print(discrepency_u)
        print(discrepency_v)
        d1=abs(discrepency_u-1)+abs(discrepency_v-1)-(abs(discrepency_u)+abs(discrepency_v))
        e2=choice(left_edges)

        x=e2[0]
        y=e2[1]
        print(x)
        print(y)
        discrepency_x=nx.degree(Gadr)[x]-node_degree_dict[x]
        discrepency_y=nx.degree(Gadr)[y]-node_degree_dict[y]
        print(discrepency_x)
        print(discrepency_y)
        d2=abs(discrepency_x+1)+abs(discrepency_y+1)-(abs(discrepency_x)+abs(discrepency_y))
        if d1+d2<0:
            Gadr.remove_edge(u,v)
            Gadr.add_edge(x,y)
            left_edges.remove(e2)
            left_edges.append(e1)
            print( "change edge")
            print(e1)
            print(e2)

    print(Gadr.edges())
    print(left_edges)
    return Gadr



def abm(G,edge_pro_dict,node_degree_dict):
    print("starting abm")
    Gabm=nx.Graph()
    Gtemp=nx.Graph()

    for each_node in G.nodes():
        Gabm.add_node(each_node)
        Gtemp.add_node(each_node)

    for each_edge in G.edges():
        Gtemp.add_edge(each_edge[0],each_edge[1])

    node_degree_dict_round={}
    for each_node in node_degree_dict:
        node_degree_dict_round[each_node]=int(round(node_degree_dict[each_node]))

    letf_edges=[]
    while(len(Gtemp.edges())!=0):
        e1=choice(Gtemp.edges())
        u=e1[0]
        v=e1[1]
        Gtemp.remove_edge(u,v)
        if nx.degree(Gabm)[u]<node_degree_dict_round[u] and nx.degree(Gabm)[v]<node_degree_dict_round[v]:
           Gabm.add_edge(u,v)
        else:
            letf_edges.append(e1)
    print( "abm phase 1")
    print(Gabm.edges())
    print(letf_edges)

    a_group=[]
    b_group=[]
    c_group=[]
    for each_node in Gabm.nodes():
        disu=nx.degree(Gabm)[each_node]-node_degree_dict[each_node]

        if disu<=-0.5:
            a_group.append(each_node)
        elif disu>-0.5 and disu<0:
            b_group.append(each_node)
        else:
            c_group.append(each_node)
    print (a_group)
    print(b_group)
    print(c_group)
    bipartite={}
    for each_edge in letf_edges:
        a=each_edge[0]
        b=each_edge[1]
        if b in a_group and a in b_group:
            t=a
            a=b
            b=t
        if a in a_group and b in b_group:
            disa=nx.degree(Gabm)[a]-node_degree_dict[a]
            disb=nx.degree(Gabm)[b]-node_degree_dict[b]
            we=abs(disa)+2*abs(disb)-abs(1+disa)-1
            if we>0:
                bipartite[(a,b)]=we

    print(bipartite)
    q_order=sorted( bipartite.iteritems(), key=lambda d:d[1],reverse=True)
    print(q_order)
    while(len(q_order) !=0):
        edge_ab=q_order[0]
        edge_a=edge_ab[0][0]
        edge_b=edge_ab[0][1]
        print("add edge")
        print edge_a,
        print(edge_b )
        Gabm.add_edge(edge_a,edge_b)
        dis_edge_a=nx.degree(Gabm)[edge_a]-node_degree_dict[edge_a]

        for i in bipartite.keys():
            if edge_b in i:
                print "remove edges of b",
                print (edge_b)
                print (i)
                temp=(i,bipartite[i])
                print temp
                print q_order
                q_order.remove(temp)
                bipartite.pop(i)

        if dis_edge_a>-1 and dis_edge_a<=-0.5:
            for i in bipartite.keys():
                if edge_a in i:
                    dis_edge_x=nx.degree(Gabm)[i[1]]-node_degree_dict[i[1]]
                    we=abs(dis_edge_a)+2*abs(dis_edge_x)-abs(1+dis_edge_a)-1
                    if we >0:
                        bipartite[i]=we
                        q_order=sorted( bipartite.iteritems(), key=lambda d:d[1],reverse=True)
                    else:
                        print "remove edges of a",
                        print (edge_a)
                        print (i)
                        temp=(i,bipartite[i])
                        print temp
                        print q_order
                        q_order.remove(temp)
                        bipartite.pop(i)

        elif dis_edge_a>-0.5:

             for i in bipartite.keys():
                if edge_a in i:
                     temp=(i,bipartite[i])
                     q_order.remove(temp)
                     bipartite.pop(i)
    return Gabm























