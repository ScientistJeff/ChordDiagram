__author__ = 'jeff'
import csv
import networkx
import pandas as pd
import os
import la
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/jeff/PycharmProjects/ChordDiagram')

with open("UNTRADEDRelationships_NAICS.csv") as f:
    data = pd.DataFrame(pd.read_csv(f))
    peoplelist = data['Source'].unique()
    targetlist = data['Target'].unique()
    connectionlist = []

B = networkx.Graph()
#B.add_nodes_from(peoplelist,bipartite=0)

B.add_nodes_from(targetlist,bipartite=1)
newlist = []
for index,row in data.iterrows():
    newlist.append((row['Source'],row['Target']))
B.add_edges_from(newlist)
B2 = networkx.projected_graph(B,targetlist,multigraph=True)
mymatrix = networkx.to_numpy_matrix(B2, dtype=np.float16)
label = [list(targetlist),list(targetlist)]
mylarry = la.larry(mymatrix,label, dtype=float)
mylarry.tofile('newlarry2.csv')

thindata = data.iloc[:,[2,3,4]]
thinnodup = thindata.drop_duplicates()
thinnodup.to_csv('listofcompanies.csv')
