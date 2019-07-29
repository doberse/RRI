# -*- coding: utf-8 -*-

import seaborn as sns
import pandas as pd
import math
import matplotlib.pyplot as plt

df=pd.read_csv('./input_data/degrees_of_3networks.txt',sep='\t')
l=[math.log10(x) for x in df['Degree']]
df['Degrees (log10)']=l
plt.figure(figsize=(6,6))
xname='Degrees (log10)'
sns.violinplot(y='Type',x=xname,data=df,order=['RRI','PPI','Co-expression'])

fsize=20

plt.xlim((0,5))
plt.xticks(fontsize=fsize)
plt.xlabel(xname,fontsize=fsize)

plt.ylabel('')
plt.yticks(rotation=90,fontsize=fsize,va='center')
plt.tick_params(length=0)
plt.savefig('distribution_of_degrees_of_3networks',dpi=300)
