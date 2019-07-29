# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

with open('./input_data/hub_nodes.txt') as r:
    RNAnet=set([l.strip() for l in r])
with open('./input_data/BC-related_genes.txt') as r:
    PPI=set([l.strip() for l in r])
with open('./input_data/DEGs.txt') as r:
    coEx=set([l.strip() for l in r])

plt.figure()
venn3((RNAnet,PPI,coEx),('Hub nodes','BC-related genes','DEGs'))
plt.savefig('overlapping_of_hub_nodes_DEGs_BC-related_genes',dpi=300)
