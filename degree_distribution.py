# -*- coding: utf-8 -*-

import seaborn as sns
import pandas as pd
import math
import matplotlib.pyplot as plt

df=pd.read_csv('./input_data/node_degree_in_RRI_network.txt',sep='\t',index_col='Molecule')
df['Node degree (log10)']=[math.log10(x) for x in df['Degree']]#normalized by log10 transformation

plt.figure(figsize=(25,6))
yname='Node degree (log10)'
sns.violinplot(x='Type',y=yname,data=df,
               order=['mRNA','miRNA','lncRNA','rRNA','circRNA','tRNA','pseudogene','snRNA','snoRNA','scRNA','miscRNA','other'])
plt.ylim((0,5))
fsize=30
plt.yticks(fontsize=fsize)
plt.xticks(rotation=30,fontsize=fsize)
plt.xlabel('')
plt.ylabel(yname,fontsize=fsize)
plt.tick_params(length=0)
plt.savefig('distribution_of_node_degrees_in_RRI_network',dpi=300)
