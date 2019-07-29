# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib_venn import venn3
from itertools import islice

def take_ENSG_pair(nm):
    ll=[]
    r=open(nm)
    for l in r:
        ws=l.strip().split('\t')
        a=ws[0].split('~')
        if a[1]!='*':
            q1=a[1]            
        else:
            q1=ws[0]
        b=ws[1].split('~')
        if b[1]!='*':
            q2=b[1]             
        else:
            q2=ws[1]
        qx=sorted([q1,q2])
        ll.append(tuple(qx))
    r.close()
    lz=sorted(set(ll))
    return lz

RNAnetENSG=take_ENSG_pair('./input_data/edges_of_RRI_network.txt')#edges of RRI network

PPIensg=take_ENSG_pair('./input_data/edges_of_PPI_network.txt')#edges of PPI network

hsa2ensg={}
with open('./input_data/pre-miRNA_to_ensembl_id.txt') as r:
    for l in r:
        ws=l.strip().split('\t')
        hsa2ensg[ws[0]]=ws[1]
ll=[]
with open('./input_data/edges_of_co-expression_network.txt') as r:
    for l in islice(r,1,None):
        ws=l.strip().split('\t')
        for i in [0,1]:
            if 'ENSG' not in ws[i]:
                if hsa2ensg[ws[i]]!='*':
                    ws[i]=hsa2ensg[ws[i]]
        qx=sorted(ws[0:2])
        ll.append(tuple(qx))
coEx=sorted(set(ll))#edges of co-expression network

plt.figure()
venn3((set(RNAnetENSG),set(PPIensg),set(coEx)),('RRI','PPI','Co-expression'))
plt.title('Overlapping of edges')
plt.savefig('venn_for_intersection_of_edges.png',dpi=300)
