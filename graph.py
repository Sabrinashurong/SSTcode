from collections import defaultdict
import numpy as np
import pandas as pd
import sys
sys.setrecursionlimit(800000)
# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, verticesNum,verticsindexlist = []):
        self.Nv = verticesNum  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        if verticsindexlist == []:
            self.verticsindexlist = list(range(verticesNum))
        else:
            self.verticsindexlist = verticsindexlist

        self.visited = np.zeros(verticesNum, dtype=np.int32)
        self.leader = np.zeros(verticesNum, dtype=np.int32)
        self.time = 0
        self.finishingtime = np.zeros(verticesNum, dtype=np.int32)
        self.stack = []
    # Python implementation of Kosaraju's algorithm to print all SCCs
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSorder(self,v,leader_s):
        # Mark the current node as visited 
        self.visited[v] = 1
        self.leader[v] = leader_s

        #Recur for all the vertices adjacent to this vertex 
        for v_i in self.graph[v]:
            if self.visited[v_i] == 0:
                self.DFSorder(v_i,leader_s)
        self.time = self.time + 1
        self.finishingtime[v] = self.time
        self.stack.append(v)
    def DFS(self):
        for i in range(self.Nv):
            vertice_i = self.verticsindexlist[self.Nv - 1 - i]
            if self.visited[vertice_i] == 0:
                leaderTrack = vertice_i
                self.DFSorder(vertice_i,leaderTrack)
        # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.Nv, list(self.stack)) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 

    def returnStack(self):
        return self.stack
    def returnFinishingtime(self):
        return self.finishingtime