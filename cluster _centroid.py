
import numpy as np
import pandas as pd
from copy import deepcopy
import random
import sys
IN = str(input('Input file path and value of k-:  '))
for i in range(1,len(IN)):
    if IN[-i]=='t' :
        break
    else :
        pass
path = IN[:len(IN)-i+1]
k = int(IN[-i+2:])

data = pd.read_table(path,delim_whitespace=True,header=None)



num_row,num_col = data.shape
if k > num_row :
    print('The value of k must be less than total given data points')
    Exit = input('PRESS ENTER TO EXIT')
    sys.exit()
else :
    pass

X = np.empty(shape=data.shape)
for x in range(num_row):
    X[x] = data.iloc[[x],:]

# Euclidean Distance Caculator
def dist(a,b) :
    dlist = []
    for x in range(len(b)) :
        l = (a-b)**2
        dlist.append(np.sqrt(sum(l[x])))
    return(dlist)
    

# random generator for k centroids
Y = (list(X))
C = np.array(random.sample(Y,k))

# To store the value of centroids when it updates
C_old = np.zeros(C.shape)


# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(X))


# Error func. - Distance between new centroids and old centroids
error = (dist(C, C_old))


# Loop will run till the error becomes zero
while (sum(error)) != 0:
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        dl = dist(X[i], C)
        cluster = dl.index(min(dl))
        clusters[i] = cluster

    # Storing the old centroid values
    C_old = deepcopy(C)
    
    # Finding the new centroids by taking the average value
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old)
   
    
print(C)

# for saving output as text file Enter path of output text file
output_path = str(input('Enter path of the output text file to save the cluster points-: '))
with open(output_path,"w") as f:
    f.write("\n".join(" ".join(map(str, x)) for x in C))

Exit = input('Data saved in output file.\nPRESS ENTER TO EXIT')
