# -*- coding: utf-8 -*-

import pandas as pd
import networkx as nx

def gdm(i):
    if ws[i] not in g2d:
        g2d[ws[i]]=ws[2]
    else:
        g2d[ws[i]]='&'.join(list(set(g2d[ws[i]].split('&'))|set(ws[2].split('&'))))

#Gene to disease
df=pd.read_csv('input_data/disease_gene.csv',dtype=object)
g2d={}
for l in df.index:
    ws=df.loc[l,:].values.tolist()
    if ws[0]!='*':
        gdm(0)
    if ws[1]!='*':
        gdm(1)

#Node to disease in the co-expression network
r=open('input_data/Co-expression_node.csv')
r.readline()
node2disease={}
for l in r:
    ws=l.strip().split(',')
    if ws[2] in g2d:
        node2disease[ws[0]]=set(g2d[ws[2]].split('&'))
r.close()
ks=list(node2disease.keys())

#Calculate the shortest path lengths
edge=[]
with open('input_data/Co-expression_network_part1.txt') as r:
    for l in r:
        edge.append(tuple(l.strip().split('\t')))
with open('input_data/Co-expression_network_part2.txt') as r:
    for l in r:
        edge.append(tuple(l.strip().split('\t')))
G=nx.Graph()
G.add_edges_from(edge)
num=len(ks)
w=open('SPL_disease_CoEx_network.csv','w')
w.write(','.join(['Node1','Node2','Shortest path length'])+'\n')
for i in range(num):
    a=ks[i]
    for j in range(i+1,num):
        b=ks[j]
        if len(node2disease[a]&node2disease[b])>0:#Within the same disease
            if nx.has_path(G,a,b):
                w.write(','.join([a,b,str(nx.shortest_path_length(G,a,b))])+'\n')
w.close()
