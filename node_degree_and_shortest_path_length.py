# -*- coding: utf-8 -*-

import seaborn as sns
import pandas as pd
import math
from scipy import stats
import matplotlib.pyplot as plt

def dict_list(dic,s,t):
    if s not in dic:
        dic[s]=[t]
    elif t not in dic[s]:
        dic[s].append(t)
def dict_mashup(dic):
    for k in dic:
        if len(dic[k])==1:
            dic[k]=dic[k][0]

def ttest(a,b):
    s,p=stats.levene(a,b)
    if p<0.05:
        equal_valv=False
    else:
        assert False
        equal_valv=True
    t,p=stats.ttest_ind(a,b,equal_var=equal_valv)
    return t,p

#Distribution of degrees of BC-related genes and randomly selected nodes in the RRI network
df=pd.read_csv('./input_data/degrees_of_BC-gene_and_random_nodes_in_RRI_network.txt',sep='\t')
df=df.set_index(['Label'],drop=False)
df['Degrees (log10)']=[math.log10(x) for x in df['Degree']]#normalized by log10 transformation
t,p=ttest(df.loc['BC','Degree'],df.loc['Random','Degree'])
plt.figure(figsize=(5.5,5.5))
yname='Degrees (log10)'
sns.violinplot(x='Label',y=yname,data=df)
plt.ylim((0,5))

fsize=20
plt.ylabel(yname,fontsize=fsize)
plt.yticks(fontsize=fsize)
if p>0:
    plt.xlabel('T-statistic: %.1f (p = %.1e)'%(t,p),fontsize=fsize)
else:
    plt.xlabel('T-statistic: %.1f (p << 0.01)'%t,fontsize=fsize)
plt.xticks(fontsize=fsize)

plt.tick_params(length=0)
plt.savefig('distribution_of_degrees_of_BC-gene_and_random_nodes_in_RRI_network.png',dpi=300)

#Distribution of shortest path lengths of BC-related genes and randomly selected nodes in the RRI network
df2=pd.read_csv('./input_data/shortest_path_lengths_of_BC-gene_and_random_nodes_in_RRI_network.txt',sep='\t')
df2=df2.set_index(['label'],drop=False)
t,p=ttest(df2.loc['BC','Shortest path length'],df2.loc['Random','Shortest path length'])
plt.figure(figsize=(5.5,5.5))
yname='Shortest path length'
sns.boxplot(x='label',y=yname,data=df2)

fsize=20
plt.ylabel(yname,fontsize=fsize)
plt.yticks(fontsize=fsize)
if p>0:
    plt.xlabel('T-statistic: %.1f (p = %.1e)'%(t,p),fontsize=fsize)
else:
    plt.xlabel('T-statistic: %.1f (p << 0.001)'%t,fontsize=fsize)
plt.xticks(fontsize=fsize)

plt.tick_params(length=0)
plt.savefig('distribution_of_shortest_path_lengths_of_BC-gene_and_random_nodes_in_RRI_network.png',dpi=300)
