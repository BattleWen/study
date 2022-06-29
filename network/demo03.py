import numbers
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import numpy #用于显示中文字符
import pandas as pd
import os
import random


filename = "blocks.txt"
G = nx.Graph()  # 一个空的无向图G
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head, tail)
    
#度中心性
deg=G.degree()
#特征向量中心性
ec = nx.eigenvector_centrality(G)
ec_rank=[]
for node, value in ec.items():
    ec_rank.append(value)
# #pagerank中心性
# pr=nx.pagerank(G,alpha=0.85)
# pr_rank=[]
# for node, value in pr.items():
#     pr_rank.append(value)
#中介中心性 betweenness centrality
bc = nx.betweenness_centrality(G)
bc_rank=[]
for node, value in bc.items():
    bc_rank.append(value*(len(G.nodes())-1)*((len(G.nodes())-2))/2)
#接近中心性 closeness centrality
cc=nx.closeness_centrality(G)
cc_rank=[]
for node, value in cc.items():
    cc_rank.append(1/value)

ranks = []
for i in range(len(G.nodes())):
    ranks.append(0.4673*deg[i]+0.2772*ec_rank[i]+0.1601*cc_rank[i]+0.0954*bc_rank[i])

nodes = sorted(G.nodes(), key=lambda n: ranks[n],reverse=True)

number_necks = 3  #瓶颈节点个数
threshold = 2 #距离阈值
distances = [] #节点到瓶颈节点之间的距离
for i in range(len(G.nodes())):
    distances.append(0.0)

min_distance = 100000.00
min_index = 0

for i in range(len(G.nodes())):
    for j in range(number_necks):
        temp = nx.shortest_path_length(G, source=i, target=nodes[j])
        distances[i] = distances[i] + temp


for i in range(len(G.nodes())):
        if  distances[i] < min_distance :
            min_distance = distances[i]
            min_index = i

#第一轮直接加边

temp = len(G.nodes()) #temp = 11
G.add_node(temp)
G.add_edge(min_index,temp)

#第二轮选择加边
temp2 = len(G.nodes()) #temp2 = 12
G.add_node(temp2)
G.add_edge(temp2,temp)
Ged = 4

#度中心性
deg=G.degree()
#特征向量中心性
ec = nx.eigenvector_centrality(G)
ec_rank=[]
for node, value in ec.items():
    ec_rank.append(value)
# #pagerank中心性
# pr=nx.pagerank(G,alpha=0.85)
# pr_rank=[]
# for node, value in pr.items():
#     pr_rank.append(value)
#中介中心性 betweenness centrality
bc = nx.betweenness_centrality(G)
bc_rank=[]
for node, value in bc.items():
    bc_rank.append(value*(len(G.nodes())-1)*((len(G.nodes())-2))/2)
#接近中心性 closeness centrality
cc=nx.closeness_centrality(G)
cc_rank=[]
for node, value in cc.items():
    cc_rank.append(1/value)

ranks = []
for i in range(len(G.nodes())):
    ranks.append(0.4673*deg[i]+0.2772*ec_rank[i]+0.1601*cc_rank[i]+0.0954*bc_rank[i])

weights = []
for i in range(temp,len(G.nodes())):
    weights.append(ranks[i])

# #第三轮选择加边
# temp3 = len(G.nodes()) #temp3 = 13
# G.add_node(temp3)
# a = []
# for i in range(temp,len(G.nodes())):
#     a.append(i)
# b= random.choices(a,weights,k=1)
# G.add_edge(temp3,b[0])
 
#循环选择加边

a = []
for i in range(temp,len(G.nodes())):
    a.append(i)

while ranks[min_index] > ranks[temp]:
    #第三轮选择加边
    temp3 = len(G.nodes()) #temp3 = 13
    G.add_node(temp3)
    b = random.choices(a,weights,k=1)
    G.add_edge(temp3,b[0])
    Ged = Ged + 2
    a.append(temp3)

    #度中心性
    deg=G.degree()
    #特征向量中心性
    ec = nx.eigenvector_centrality(G)
    ec_rank=[]
    for node, value in ec.items():
        ec_rank.append(value)
    #中介中心性 betweenness centrality
    bc = nx.betweenness_centrality(G)
    bc_rank=[]
    for node, value in bc.items():
        bc_rank.append(value*(len(G.nodes())-1)*((len(G.nodes())-2))/2)
    #接近中心性 closeness centrality
    cc=nx.closeness_centrality(G)
    cc_rank=[]
    for node, value in cc.items():
        cc_rank.append(1/value)

    ranks = []
    for i in range(len(G.nodes())):
        ranks.append(0.4673*deg[i]+0.2772*ec_rank[i]+0.1601*cc_rank[i]+0.0954*bc_rank[i])
    
    weights = []
    for i in range(temp,len(G.nodes())):
        weights.append(ranks[i])

print(Ged)

e = G.edges()
e2 = list(e)
head = []
for i in range(len(e2)):
    head.append(-1)
tail = []
for i in range(len(e2)):
    tail.append(-1)
for i in range(len(e2)):
    head[i],tail[i] = e2[i]
with open("blocks_output.txt",'w') as f:
    for i in range(len(e2)):
        f.writelines(str(head[i]) + ' '+ str(tail[i])+'\n')
# with open("output.txt",'w') as f:
#     for i in range(len(e2)):
#         head,tail = str(e2[i])
#         f.writelines('head' + ' '+'tail')
    

# with open("output.txt",'w') as f:
#     for i in range(len(e)):
#         print(e[i])


nx.draw(G,with_labels=True)
plt.show()