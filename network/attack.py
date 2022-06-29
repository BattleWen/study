import numbers
from operator import length_hint
from re import A
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import numpy #用于显示中文字符
import pandas as pd
import os
import random

from torch import GraphExecutorState


filename = "blocks.txt"
G = nx.Graph()  # 一个空的无向图G
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head, tail) 

# def save_graph(graph,pos,file_name):
#         #initialze Figure
#         plt.figure(num=None, figsize=(20, 20), dpi=80)
#         plt.axis('off')
#         fig = plt.figure(1)
#         nx.draw_networkx_nodes(graph,pos)
#         nx.draw_networkx_edges(graph,pos)
#         nx.draw_networkx_labels(graph,pos)

#         cut = 1.00
#         xmax = cut * max(xx for xx, yy in pos.values())
#         ymax = cut * max(yy for xx, yy in pos.values())
#         plt.xlim(0, xmax)
#         plt.ylim(0, ymax)

#         plt.savefig(file_name,bbox_inches="tight")
#         plt.close()
#         del fig

def attack(graph,numbers,centrality_metric):
        graph = graph.copy()
        steps = numbers
        ranks = centrality_metric
        nodes = sorted(graph.nodes(), key=lambda n: ranks[n])
        
        max_length = 0
        #Generate spring layout
        # pos = nx.spring_layout(graph)

        for i in range(steps):
            graph.remove_node(nodes.pop())
            # file_name = './sim/'+str(steps)+'.png'
            # save_graph(graph,pos,file_name)
        # for i in nx.connected_components(graph):
        #     print(i)
        H = list(graph.subgraph(c) for c in nx.connected_components(graph))#各个连通分量的子图
        max_length = 0
        max_index = 0
        for i in range(nx.number_connected_components(graph)):
            if len(H[i]) > max_length:
                max_length = len(H[i])
                max_index = i
        print("最大连通分量的节点数：",max_length) #最大连通子图的节点数
        
        max_diameter = 0
        for i in range(nx.number_connected_components(graph)):
            if nx.diameter(H[i]) > max_diameter:
                max_diameter = nx.diameter(H[i])
        print("网络直径：",float(max_diameter))

        # average_clustering = nx.average_clustering(H[max_index])#平均聚类系数
        # print("平均聚类系数：",float(average_clustering))
        

        i_length = 0
        sum_length = 0
        for i in range(nx.number_connected_components(graph)):
            if len(H[i]) > 1:
                i_length = nx.average_shortest_path_length(H[i])*len(H[i])*(len(H[i])+1)/2
                sum_length = sum_length + i_length
        Nodes = nx.number_of_nodes(G)       
        average_length = 2*sum_length/(Nodes*(Nodes+1))#平均最短路径
        print('平均路径长度', float(average_length))

        sum_len = 0
        for i in range(nx.number_connected_components(graph)):
            if len(H[i]) > 1:
                sum_len = sum_len + len(H[i])
        print("失效节点比例：",(len(G.nodes())-sum_len)/len(G.nodes()))
        #输出网络的边集
        e = graph.edges()
        e2 = list(e)
        head = []
        for i in range(len(e2)):
            head.append(-1)
        tail = []
        for i in range(len(e2)):
            tail.append(-1)
        for i in range(len(e2)):
            head[i],tail[i] = e2[i]
        with open("blocks_ec_50%.txt",'w') as f:
            for i in range(len(e2)):
                f.writelines(str(head[i]) + ' '+ str(tail[i])+'\n')
        # nx.draw(graph,with_labels=True)
        # plt.show()

def random_attack(graph,numbers):
    graph = graph.copy()
    steps = numbers
    max_length = 0

    for i in range(steps):
        a = list(graph.nodes())
        node = random.choice(a)
        graph.remove_node(node)
    H = list(graph.subgraph(c) for c in nx.connected_components(graph))#各个连通分量的子图
    max_length = 0
    max_index = 0
    for i in range(nx.number_connected_components(graph)):
        if len(H[i]) > max_length:
            max_length = len(H[i])
            max_index = i
    print("最大连通分量的节点数：",max_length) #最大连通子图的节点数
    
    max_diameter = 0
    for i in range(nx.number_connected_components(graph)):
        if nx.diameter(H[i]) > max_diameter:
            max_diameter = nx.diameter(H[i])
    print("网络直径：",float(max_diameter))

    # average_clustering = nx.average_clustering(H[max_index])#平均聚类系数
    # print("平均聚类系数：",float(average_clustering))
    

    i_length = 0
    sum_length = 0
    for i in range(nx.number_connected_components(graph)):
        if len(H[i]) > 1:
            i_length = nx.average_shortest_path_length(H[i])*len(H[i])*(len(H[i])+1)/2
            sum_length = sum_length + i_length
    Nodes = nx.number_of_nodes(G)       
    average_length = 2*sum_length/(Nodes*(Nodes+1))#平均最短路径
    print('平均路径长度', float(average_length))

    sum_len = 0
    for i in range(nx.number_connected_components(graph)):
        if len(H[i]) > 1:
            sum_len = sum_len + len(H[i])
    print("失效节点比例：",(len(G.nodes())-sum_len)/len(G.nodes()))
    
    e = graph.edges()
    e2 = list(e)
    head = []
    for i in range(len(e2)):
        head.append(-1)
    tail = []
    for i in range(len(e2)):
        tail.append(-1)
    for i in range(len(e2)):
        head[i],tail[i] = e2[i]
    with open("arenas_email_random_50%.txt",'w') as f:
        for i in range(len(e2)):
            f.writelines(str(head[i]) + ' '+ str(tail[i])+'\n')
    # nx.draw(graph,with_labels=True)
    # plt.show()
    
        

deg = G.degree()


cc=nx.closeness_centrality(G)
cc_rank=[]
for node, value in cc.items():
    cc_rank.append(value)

ec = nx.eigenvector_centrality(G)
ec_rank=[]
for node, value in ec.items():
    ec_rank.append(value)

bc = nx.betweenness_centrality(G)
bc_rank=[]
for node, value in bc.items():
    bc_rank.append(value) 

# random_attack(G,567)
attack(G,19,ec_rank)


# nx.draw(G,with_labels=True)
# plt.show()