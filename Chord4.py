__author__ = 'jeff'
import csv
import networkx
import pandas as pd
import os
import la
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

os.chdir('/Users/jeff/PycharmProjects/ChordDiagram')

with open("UNTRADEDRelationships_NAICS_9-27b.csv") as f:
    data = pd.DataFrame(pd.read_csv(f))
    peoplelist = data['Person_Id'].unique()
    targetlist = data['Business_Id'].unique()
    connectionlist = []

B = networkx.Graph()
B.add_nodes_from(peoplelist,bipartite=0)

B.add_nodes_from(targetlist,bipartite=1)
newlist = []
for index,row in data.iterrows():
    newlist.append((row['Person_Id'],row['Business_Id']))
B.add_edges_from(newlist)
print(len(B.nodes()))
print networkx.is_connected(B)
print len(targetlist)
print len(peoplelist)
print newlist[0:5]
top_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']==0)
bottom_nodes = set(B) - top_nodes
print len(top_nodes)
print len(bottom_nodes)
B2 = networkx.projected_graph(B,bottom_nodes,multigraph=True)
mymatrix = networkx.to_numpy_matrix(B2, dtype=np.float16)

print len(mymatrix[:,1])
print len(B2.nodes())
label = [B2.nodes(),B2.nodes()]
mylarry = la.larry(mymatrix,label, dtype=float)
mylarry.tofile('newlarry2.csv')

thindata = data.iloc[:,[2,3,4,5]]
thinnodup = thindata.drop_duplicates()
thinnodup.to_csv('listofcompanies.csv')
