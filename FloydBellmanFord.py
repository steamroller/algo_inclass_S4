# -*- coding: utf-8 -*-
"""
Digraph Shortest Paths
Floyd + Bellman-Ford
"""

from algopy import graph


inf = float('inf')

def Floyd(G):
    n = G.order
    dist = []
    p = []
    for x in range(n):
        dist.append([])
        p.append([])
        for y in range(n):
            if (x, y) in G.costs:
                dist[x].append(G.costs[(x, y)])
            else:
                dist[x].append(inf)
            p[x].append(x)
            
    for i in range(n):
        for x in range(n):
            for y in range(n):
                if dist[x][i] + dist[i][y] < dist[x][y]:
                    dist[x][y] = dist[x][i] + dist[i][y]
                    p[x][y] = p[i][y]
    
    return (dist, p)
    
#------------------------------------------------------------------------------
    
def BellmanFord(G, src):
    """
    returns a tuple (boolean, dist, p):
        boolean = is there a negative circuit
    """

    dist = [inf] * G.order    
    dist[src] = 0
    p = [-1] * G.order
    n = G.order
    changes = True
    while n > 0 and changes:
        changes = False
        for x in range(G.order-1, -1, -1):
            if dist[x] != inf:
                for y in G.adjlists[x]:
                    if dist[x] + G.costs[(x, y)] < dist[y]:
                        dist[y] = dist[x] + G.costs[(x, y)]
                        p[y] = x
                        changes = True
        n -= 1
    return (changes, dist, p)

#------------------------------------------------------------------------------
# optimization?
    
from algopy import queue

def BellmanFordOpti(G, src):
    dist = [inf] * G.order    
    dist[src] = 0
    p = [-1] * G.order
    n = G.order     
    q = queue.Queue()
    q.enqueue(src)
    inQueue = [False] * G.order
    inQueue[src] = True
    q2 = queue.Queue()    
    while n > 0 and not q.isempty():
        x = q.dequeue()
        inQueue[x] = False
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
                if not inQueue[y]:
                    q2.enqueue(y)
                    inQueue[y] = True
        if q.isempty():    # level change
            q = q2
            q2 = queue.Queue()
            n -= 1
    return (not q.isempty(), dist, p)
    
    
    
    
    
    
    
