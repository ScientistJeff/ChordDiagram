__author__ = 'jeff'




import csv
import networkx
import itertools
import pandas as pd
import collections
import matplotlib.pyplot as plt
import numpy as np
import os
import la

os.chdir('/Users/jeff/PycharmProjects/ChordDiagram')

with open ("UntradedRelationshipsEDGES.csv") as f:
    data = pd.DataFrame(pd.read_csv(f))
#companylist = data['Target'].unique()

    peoplelist = data['Source'].unique()
    targetlist = data['Target'].unique()
    connectionlist = []

#for i in companylist:
# memberList = []

# memberlist=data['Source'][data.Target==i].tolist()
# connectionlist += (list(itertools.permutations(memberlist,2)))

# resultdict=collections.defaultdict(list)


    for i in targetlist:
        global memberlist
        memberlist = []
        memberlist=data['Source'][data.Target==i].tolist()
        print memberlist
        cxlist = (list(itertools.permutations(memberlist,2)))
        for n in cxlist:
            mytuple = tuple([n,i])
            connectionlist += [mytuple]
    #print mytuple
    resultdict=collections.defaultdict(list)

#for x in connectionlist:
# resultdict[x[0]].append(x[1])
#

for x in connectionlist:
    resultdict[x[0]].append(x[1])
#resultdict
G=networkx.from_dict_of_lists(resultdict)

mymatrix = networkx.to_numpy_matrix(G)

mymatrix.shape

mymatrix[0,:]
#G.nodes()
label = [memberlist,memberlist]
mylarry = la.larry(mymatrix,label, dtype=float)

