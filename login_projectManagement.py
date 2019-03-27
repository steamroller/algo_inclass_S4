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
    
    #FIXME
    
    return (G, G_1, din, dout)

def BellmanForProject(G, src, din):
    """
    return dist: the longuest paths from src to all vertices
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
    
    #FIXME
    
    return None

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
