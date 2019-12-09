# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd

#Other nodes connected by one node
r=open('input_data/BC-related_RRI_network.txt')
ll=r.readlines()
r.close()
rna_pairs=[]
node_to_nodes={}
for l in ll:
    ws=l.strip().split('\t')
    qx=sorted(ws[0:2])
    rna_pairs.append((qx[0],qx[1]))
    for i in [0,1]:
        if i==0:
            j=1
        else:
            j=0
        if qx[i] not in node_to_nodes:
            node_to_nodes[qx[i]]=[qx[j]]
        else:
            node_to_nodes[qx[i]].append(qx[j])

#Dictionary of Node No.
r=open('input_data/RRI_node.csv')
r.readline()
no2node={}
for l in r:
    ws=l.strip().split(',')
    no2node[ws[0]]='~'.join(ws[1:7])
r.close()

#Sort nodes by node degree
node_degree={}
for k in node_to_nodes:
    node_degree[k]=len(node_to_nodes[k])
df=pd.DataFrame(node_degree,index=['Degree'])
df=df.sort_values(by='Degree',axis=1,ascending=False)
nodes=df.columns.values

#Compute the relative conectivity of subgraphs
G=nx.Graph()
node_G=[]
w=open('RC_in_BC-related_RRI_network.csv','w')
w.write('Node,No.,Relative connectivity\n')
k=0
lim=len(nodes)
while k<lim:
    node_key=nodes[k]
    node_G.append(node_key)
    G.add_node(node_key)#Add the node in subgraphs
    for node in node_G:
        if node in set(node_to_nodes[node_key]):
            G.add_edge(node_key,node)#Add the edge in subgraphs
    largest_components=max(nx.connected_components(G),key=len)
    k+=1
    w.write(no2node[node_key]+','+str(k)+','+str(len(largest_components)/float(len(node_G)))+'\n')
w.close()
