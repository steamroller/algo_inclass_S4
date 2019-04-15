# -*- coding: utf-8 -*-
"""
MST
@author: Nathalie
"""


from algopy import graph
from algopy import heap_spe as heap     # heap with index table for vertices


inf = float('inf')


#------------------------------------------------------------------------------
# Prim: with a heap like Dijkstra


def Prim(G, x = 0):
    T = graph.Graph(G.order, False, costs = True)
    d = [inf] * G.order
    p = [-1] * G.order
    M = [False] * G.order # vertices already in solution
    H = heap.Heap(G.order)
    d[x] = 0    #useless
    M[x] = True
    n = 0
    while n < G.order - 1:
        for y in G.adjlists[x]:
            if not M[y] and G.costs[(x, y)] < d[y]:
                d[y] = G.costs[(x, y)]
                p[y] = x
                H.update(y, d[y])
        
        if H.isEmpty():
            raise Exception ("Not connected")
        (_, x) = H.pop()  
        M[x] = True
        T.addedge(x, p[x], d[x])        
        n += 1
    return T



from union_find import union2
import heapq   # simple heaps (without indexes...)


def Kruskal(G):
    H = []  
    for x in range(G.order):
        for y in G.adjlists[x]:
            if x > y:
                heapq.heappush(H, (G.costs[(x, y)], x, y))

    p = [-1] * G.order # to use with union2
    T = graph.Graph(G.order, directed=False, costs=True)
    n = 0
    while n < G.order - 1 and H:
        (c, x, y) = heapq.heappop(H)
        if union2(x, y, p):
            T.addedge(x, y, c)
            n = n + 1
    if n < G.order - 1:
        raise Exception("Not connected")
    return T

    
