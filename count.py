# -*- coding: utf-8 -*-

from pyecharts import Polar
from pyecharts import Pie
import pandas as pd

count=pd.read_csv('./input_data/numbers_of_RRI_and_RNA_in_RRI_network.csv', index_col='RNA_type')

rna=[x for x in count.index if '-' not in x]#Select RNA
rna_number=count.loc[rna,'Count']#Numbers of RNA of each type
polar=Polar()
polar.add('',rna_number, angle_data=rna, type="barAngle")
polar.render(path='./RNA_numbers_in_RRI_network.html')

rri=[x for x in count.index if '-' in x]#Select RNA-RNA interaction
rri_number=count.loc[rri,'Count']#Numbers of RNA-RNA interaction of each type
pie=Pie()
pie.add('',rri,rri_number,center=[50,50],rasetype='radius',radius=[30, 75],is_legend_show=False,is_label_show=False)
pie.render(path='./RRI_numbers_in_RRI_network.html')
