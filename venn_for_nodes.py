# -*- coding: utf-8 -*-

from matplotlib_venn import venn3
import matplotlib.pyplot as plt

#Nodes of the co-expression network
with open('./input_data/genes_in_co-expression_network.txt') as r:
    coex=set()
    for l in r:
        coex.add(l.strip())
        
#Nodes of the RRI network
r=open('./input_data/node_degree_in_RRI_network.txt')
ll=r.readlines()
r.close()
RNA=set()
for l in ll[1:]:
    ws=l.strip().split('~')
    if ws[1]!='*':
        RNA.add(ws[1])
    else:
        RNA.add('~'.join(ws[0:5]))

#Nodes of the PPI network
with open('./input_data/genes_in_PPI_network.txt') as r:
    protein=set()
    for x in r:
        protein.add(x.strip())
        
plt.figure()
plt.title('Overlapping of nodes')
venn3([RNA,protein,coex],('RRI','PPI','Co-expression'))
plt.savefig('venn_for_intersection_of_nodes.png',dpi=300)
