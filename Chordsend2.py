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
B2 = networkx.projected_graph(B,targetlist,multigraph=True)
mymatrix = networkx.to_numpy_matrix(B2, dtype=np.float16)
label = [list(targetlist),list(targetlist)]
mylarry = la.larry(mymatrix,label, dtype=float)

# with open('adj_csv.csv','wb') as csvfile:
#     mywriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     mywriter.writerows(mymatrix)

np.savetxt("adj_matr2.csv",mymatrix,fmt='%3d',delimiter=",")

