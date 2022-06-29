import networkx as nx
import matplotlib.pyplot as plt
import os
import xlwt

filename = "facebook_combined.txt"
G = nx.Graph()  # 建立一个空的无向图G
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head,tail)

# #创建一个excle表格
# book = xlwt.Workbook(encoding='utf-8',style_compression=0)
# sheet = book.add_sheet('节点中心性',cell_overwrite_ok=True)
# col = ('节点编号','度值','特征向量中心性','pagerank中心性','中介中心性','接近中心性')
# for i in range(0,6):
#     sheet.write(0,i,col[i])

deg=G.degree()
#度中心性

##输出到txt文件
# fp = open("test.txt","w")
# for i in range(len(deg)):
#     fp.write(str(i))
#     fp.write(' ')
#     fp.write(str(deg[i]))
#     fp.write('\n')
# fp.close()

max_num = deg[0]
max_index = 0
for i in range(len(deg)):
    if deg[i]>max_num:
        max_num = deg[i]
        max_index = i
print("Max degree:", max_num, "Max index:", max_index)



#特征向量中心性
ec = nx.eigenvector_centrality(G)
ec_rank=[]
for node, value in ec.items():
    ec_rank.append(value)

max_num = ec_rank[0]
max_index = 0

for i in range(len(ec_rank)):
    if ec_rank[i]>max_num:
        max_num = ec_rank[i]
        max_index = i



print("Max eigenvector centrality:", max_num, "Max index:", max_index)
#pagerank中心性
pr=nx.pagerank(G,alpha=0.85)
pr_rank=[]
for node, value in pr.items():
    pr_rank.append(value)

max_num = pr_rank[0]
max_index = 0

for i in range(len(pr_rank)):
    if pr_rank[i]>max_num:
        max_num = pr_rank[i]
        max_index = i

print("Max pagerank centrality:", max_num, "Max index:", max_index)
#中介中心性 betweenness centrality
bc = nx.betweenness_centrality(G)
bc_rank=[]
for node, value in bc.items():
    bc_rank.append(value)

max_num = bc_rank[0]
max_index = 0

for i in range(len(bc_rank)):
    if bc_rank[i]>max_num:
        max_num = bc_rank[i]
        max_index = i
print("Max betweenness centrality:", max_num, "Max index:", max_index)



#接近中心性 closeness centrality
cc=nx.closeness_centrality(G)
cc_rank=[]
for node, value in cc.items():
    cc_rank.append(value)

max_num = cc_rank[0]
max_index = 0

for i in range(len(cc_rank)):
    if cc_rank[i]>max_num:
        max_num = cc_rank[i]
        max_index = i
print("Max closeness centrality:", max_num, "Max index:", max_index)


#将数据存入excel
# for i in range(len(deg)):
#     sheet.write(i+1,0,str(i))
#     sheet.write(i+1,1,str(deg[i]))
#     sheet.write(i+1,2,str(ec_rank[i]))
#     sheet.write(i+1,3,str(pr_rank[i]))
#     sheet.write(i+1,4,str(bc_rank[i]))
#     sheet.write(i+1,5,str(cc_rank[i]))
# savepath = 'D:\Desktop\pythondemo\节点中心性.xls'
# book.save(savepath)