# -*- coding: utf-8 -*-
"""
S4 - March 2019
Shortest Path Homework
@author: insert your login
"""

from algopy import graph, queue

inf = float('inf')

# example: the project "Christophe's house"

myHouse = [(2, []), (7, []), (3, [0, 1]), (1, [2]), (8, [0, 1]), (2, [3, 4]),
           (1,  [3, 4]), (1, [3, 4]), (3, [6]), (2, [8]), (1, [5, 9])]
           
          

# reminder:  
#   G = graph.Graph(order, directed=True)     # a new digraph
#   G.costs = {}                              # init costs (a dictionnary)
#   G.costs[(x, y)] = val                     # add the cost of edge (x, y)

def buildFromList(L):
    """
    L: for each task t, a pair (duration, list of tasks)
    - duration: its duration (a float) !
    - list of tasks: that have to be finished before t 
    
    returns:
        G (Graph): the digraph with last two vertices added as vitual tasks 
            task n is the beginning of the project
            task n+1 is the end
        G_1 (Graph): G reversed!
        din, dout: vectors of in- and out- degrees in G
    """
    
    n = len(L)
        
    G = graph.Graph(n+2, directed=True)
    G.costs = {}
    G_1 = graph.Graph(n+2, directed=True)
    G_1.costs = {}
    
    dout = [0] * (n+2)
    din = [0] * (n+2)

    for y in range(n):
        din[y] = len(L[y][1])       # L[y][1]: y's predecessors
        for x in L[y][1]:
            G.addedge(x, y)
            G.costs[(x, y)] = L[x][0]
            dout[x] += 1
            G_1.addedge(y, x)
            G_1.costs[(y, x)] = L[x][0]
  
    for x in range(n):
        if din[x] == 0: 
            G.addedge(n, x)     # add edges from the first task n to sources
            G_1.addedge(x, n)
            G.costs[(n, x)] = G_1.costs[(x, n)] = 0
            dout[n] += 1
            din[x] = 1
        if dout[x] == 0:          
            G.addedge(x, n+1)       # add edges from sinks to the last task (n+1)
            G_1.addedge(n+1, x)
            G.costs[(x, n+1)] = G_1.costs[(n+1, x)] = L[x][0]
            dout[x] = 1
            din[n+1] += 1

    return (G, G_1, din, dout)

def BellmanForProject(G, src, din):
    """
    return dist: the longest paths from src to all vertices
    all vertices are reachable from src
    din: the in-degree vector
    """
    dist = [-inf] * G.order
    dist[src] = 0
    q = queue.Queue()
    q.enqueue(src)
    while not q.isempty() :
        x = q.dequeue()
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] > dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
            din[y] -= 1
            if din[y] == 0:
                q.enqueue(y)
    return dist


def project(L):
    """
    L: for each task t, a pair (duration, list of tasks)
    - duration: its duration (a float) !
    - list of tasks: that have to be finished before t 
    
    returns (dates, expected time):
    - dates: for each task (earliest time, slack) 
    - the minimum expected project duration
    """
    
    n = len(L)
    (G, G_1, din, dout) = buildFromList(L)
    earliest = BellmanForProject(G, n, din)
    finish = earliest[n+1]
    late = BellmanForProject(G_1, n+1, dout)
    res = [(earliest[x], finish - late[x] - earliest[x]) for x in range(n)]
    return (res, finish)


## example:
# project(myHouse)
#Out[2]: 
#([(0, 5),
#  (0, 0),
#  (7, 4),
#  (10, 4),
#  (7, 0),
#  (15, 4),
#  (15, 0),
#  (15, 6),
#  (16, 0),
#  (19, 0),
#  (21, 0)],
# 22)
