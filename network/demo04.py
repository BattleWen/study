import os
import networkx as nx
import re

# 对图的编号重排
def relabel_graph_nodes(G):
    
    # 所有的节点
    all_nodes = list(G.nodes())

    if min(all_nodes) == 1 and max(all_nodes) == len(all_nodes):
        return G
    else:
 
        all_len = len(all_nodes) # 节点数量

        # 所有的边
        all_exist_edges = all_edges(G)
        all_exist_edges.sort()

        # 重新构造图
        H = nx.Graph()

        # 加点
        H.add_nodes_from(range(1,all_len+1))

        # 加边
        for edge in all_exist_edges:
            a = all_nodes.index(edge[0])+1
            b = all_nodes.index(edge[1])+1
            H.add_edge(a,b)


        return H
        
# 对边重排序，保证前小后大
def re_order_edge_list(lre):
    li = list()
    for i in lre:
        try:
            a = i[0]
            b = i[1]
            if a < b:
                li.append((a,b))
            elif a > b:
                li.append((b,a))
            else:
                pass
        except Exception:
            pass
    return li

# 对图进行预处理
def pre_tackle_nx_graph(G):
    
    # 获取图G的最大连通子图
    H = nx.subgraph(G,max(nx.connected_components(G),key=len))
    
    # 对图的编号重排
    H = relabel_graph_nodes(H)
    
    return H

# 图中所有已经存在的边
def all_edges(G):
    e = G.edges()    
    lre = re_order_edge_list(e)
    return lre

def tacle_data(text):
    text_name = text.split("/")[3].replace(".txt","") 
    
        
    # 读取图
    with open(text, "r") as f:
        res = f.read()
        li = res.split('\n')
    
    if "" in li:
        li.remove("")
    
    no=0
    if '.mtx' in text:
        for i in li:
            if '%' not in i:
                break
            else:
                no+=1
        li = li[no+1:]
        
    if '.edges' in text:
        for i in li:
            if '%' not in i:
                break
            else:
                no+=1
        li = li[no:]
    
    lre = list()
    for i in li:
        if "	" in i:
            line = i.split("	")
        if "," in i:
            line = i.split(",")
        if " " in i:
            line = i.split(" ")
        try:    
            
            a = int(line[0])
            b = int(line[1])
            if a < b:
                lre.append((a,b))
            elif a > b:
                lre.append((b,a))
            elif a == b:
                continue
            else:
                pass
        except Exception:
            print(text)
            exit(0)
    
    print(text_name)
    
    # 去重
    lre = list(set(lre)) 
    
    # 排序
    lre.sort()
    
    # 边数
    edges = len(lre)
    
    # 节点个数
    nodes = list(set([i for j in lre for i in j]))
    
    nodes_len = len(nodes)
    
    # 节点编号从0开始
    if min(nodes) != 1:
        new_lre = list()
        
        x = 1-min(nodes)
        
        for edge in lre:
            new_lre.append([edge[0]+x,edge[1]+x])
            
        return new_lre
            
    # 节点编号从1开始        
    elif min(nodes) == 1:
        return lre
    
    else:
        raise Exception
    



if __name__ == '__main__':
    
    #target = input('input run dir:')
    target = "newdata"

    # 指定路径下所有的图数据
    path = "./freshdata/{}/".format(target)
    jobs = os.listdir(path)
     
    obj = "finish/"
    path_f = "./freshdata/{}/".format(obj)
    
    dir_class = ['1-100','100-500','500-1000','1000-2000','2000-3000','3000-4000','5000-100000','1000-3000','all']
    
    # 按节点数分类创造文件夹
    for i in dir_class:
        is_exists = os.path.exists(path_f+i) 
        if not is_exists:
            os.mkdir(path_f+i)
    # 对图进行运算
    
    for i in jobs:
        try:
            filname = i.split(".")[0]
            text = path+i
            # 重新构造文件名

            lre = tacle_data(text)
            
            # 构造networkx 图对象
            G_nx = nx.Graph()         
            G_nx.add_edges_from(lre)
            
            # 对图进行预处理，将不连通的图取其最大连通子图，并对节点重编号
            G_nx = pre_tackle_nx_graph(G_nx)
            lre = all_edges(G_nx)
            
            edges = len(lre)
            nodes = list(set([i for j in lre for i in j]))
            nodes_len = len(nodes)
                        
                       
            try:                
                pattern = re.compile("_\d+_\d+\d$")
                useless = pattern.search(filname).group()                           
                filname = filname.replace(useless,"")
            except Exception as e:
                print(e)
            
            for i in dir_class:
                if i != "all":
                    min_d,max_d = i.split("-")
                    if nodes_len > int(min_d) and nodes_len <= int(max_d):           
                        with open(path_f+'/'+i+'/'+filname+"_"+str(nodes_len)+"_"+str(edges)+".txt", "w") as f:
                            for i in lre:
                                f.write(str(i[0])+" "+str(i[1]))
                                f.write("\n")
                else:
                    with open(path_f+'/'+i+'/'+filname+"_"+str(nodes_len)+"_"+str(edges)+".txt", "w") as f:
                        for i in lre:
                            f.write(str(i[0])+" "+str(i[1]))
                            f.write("\n")
                    
        except Exception as e:
            print(i,"error")
              