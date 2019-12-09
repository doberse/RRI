# -*- coding: utf-8 -*-

#Dictionary of Node No.
r=open('input_data/RRI_node.csv')
r.readline()
pair={}
for l in r:
    ws=l.strip().split(',')
    if ws[5]!='*':
        pair[ws[0]]=ws[5]        
    elif ws[2]!='*':
        pair[ws[0]]=ws[2]
r.close()

#Directly connected pairs
r=open('input_data/RRI_network.txt')
ll=r.readlines()
r.close()
nn=[]
for l in ll:
    ws=l.strip().split('\t')
    if ws[0] in pair:
        a=pair[ws[0]]
    else:
        continue
    if ws[1] in pair:
        b=pair[ws[1]]
    else:
        continue
    qx=sorted([a,b])
    nn.append((qx[0],qx[1]))
nzz=set(nn)
nz=sorted(nzz)
w=open('direct_pair.txt','w')
for ws in nz:
    w.write(ws[0]+'\t'+ws[1]+'\n')
w.close()

#Indirectly connected pairs
g2gs={}
for ws in nz:
    for i in [0,1]:
        if i==0:
            j=1
        else:
            j=0
        if ws[i] not in g2gs:
            g2gs[ws[i]]=[ws[j]]
        else:
            g2gs[ws[i]].append(ws[j])
ks=list(g2gs.keys())
num=len(ks)
nn=[]
for i in range(num):
    k1=set(g2gs[ks[i]])
    for j in range(i+1,num):
        qx=sorted([ks[i],ks[j]])
        if (qx[0],qx[1]) not in nzz:
            k2=set(g2gs[ks[j]])
            if k1&k2!=set([]):
                nn.append((qx[0],qx[1]))
nz2=sorted(set(nn))
w=open('indirect_pair.txt','w')
for ws in nz2:
    w.write(ws[0]+'\t'+ws[1]+'\n')
w.close()
