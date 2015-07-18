import pandas as pd
#newt = pd.Dataframe


import csv
with open('output.csv', 'wb') as fout:
    csvout = csv.writer(fout)
    for i,n in enumerate(targetlist):

            var1 = n
            var2 = data.Board[data.Target==n].unique()

            csvout.writerow([var1] + [var2])