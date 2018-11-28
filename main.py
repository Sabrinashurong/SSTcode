from graph import Graph
import numpy as np
import pandas as pd
import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

def countandoutmax5(np_array,numFind = 3):
    tt = list(np.bincount(np_array))
    array_max = []
    for i in range(numFind):
        max1 = max(tt)
        array_max.append(max1)
        tt.remove(max1)
    return array_max

def main():
    num = 68; numVertices = 320000
    df = pd.read_csv('inputdata\input_mostlyCycles_%d_%d.txt'%(num,numVertices),sep=' ',header=None)
    dfNum = len(df)

    g = Graph(numVertices)
    for i in range(dfNum):
        x = df.iloc[i,0] -1 ; y = df.iloc[i,1] -1;
        g.addEdge(x,y)
    g.DFS()

    grev = g.getTranspose()
    grev.DFS()


    #print(grev.leader)
    arrayOut = countandoutmax5(grev.leader,numFind = 5)
    print(arrayOut)
    with open('inputdata\output_mostlyCycles_%d_%d.txt'%(num,numVertices),'w') as f:
        f.write(str(arrayOut))

thread = threading.Thread(target=main)
thread.start()