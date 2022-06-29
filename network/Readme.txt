实验环境:
1.处理器为Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (8 CPUs), ~2.0GHz
2.内存16GB RAM
3.操作系统为Microsoft Windows 10
4.开发所采用的编译器是Microsoft Visual Studio Code
5.编译语言为python3.8.7

实验数据集：
1.datasets：利用demo04处理好的600多个网络数据集，节点数范围20-7000，包括社交网络，生物网络，蛋白质网络，经济网络，交通网络，电力网络等等。
2.usedData：本论文中所采用的数据集

数据分析包说明：
1.Networkx：一个由Python语言开发的图论与复杂网络建模工具。内置了常用的图与复杂网络分析算法，可以方便的进行复杂网络数据分析、仿真建模等工作

代码说明:
仅需修改代码的当前目录中的filename.txt，即可运行以下几个程序
1.demo01(excel存储)：
input：failname.txt
output：该网络结构中的最大节点中心性的节点编号，并将其存入指定的excel文件中
2.demo02(网络特征识别算法)：
input：failname.txt
output：该网络结构中的网络特征指标，以及网络的节点度分布图
3.demo03(网络抗毁性改进算法)：
input：failname.txt
output：生成虚拟拓扑后的网络边集failname_output.txt
4.demo04(数据处理代码)：
input：爬取到的网络边集 txt文件
output:将网络处理为无权无向网，同时只保留最大连通子图 txt文件
5.attack(仿真网络攻击代码):
input：原有物理拓扑结构边集 txt文件
output：攻击后的网络边集 txt文件

实验结果：
1.results：论文中数据集的csv边集文件及网路结构可视化的pdf文件