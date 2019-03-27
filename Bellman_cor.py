# -*- coding: utf-8 -*-
"""
S4 - Shortest paths
Bellman implementations
"""

from algopy import graph, stack, queue

inf = float('inf')


def dfsSuff(G, s, M, st):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            dfsSuff(G, adj, M, st)
    st.push(s)

def topologicalOrder(G, src):
    '''
    make topological order of subgraph from vertices 
    that are reachable from src
    '''
    M = [False] * G.order
    order = stack.Stack() 
    dfsSuff(G, src, M, order)
    return order
    
    
def Bellman1(G, src, dst = None):
    dist = [inf] * G.order
    dist[src] = 0
    p = [-1] * G.order
    order = topologicalOrder(G, src)
    x = order.pop()
    while not order.isempty() and (x != dst):
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
        x = order.pop()
    return (dist, p)
                
        
# another version: using the in-degree vector (only in the subgraph from reachable vertices)

def dfsIndeg(G, s, M, din):
    M[s] = True
    for adj in G.adjlists[s]:
        din[adj] += 1
        if not M[adj]:
            dfsIndeg(G, adj, M, din)
            

def indegreesSubGraph(G, src):
    din = [0] * G.order
    M = [False] * G.order
    dfsIndeg(G, src, M, din)
    return din


def Bellman2(G, src):
    dist = [inf] * G.order
    dist[src] = 0
    p = [-1] * G.order
    din = indegreesSubGraph(G, src)
    q = queue.Queue()
    q.enqueue(src)
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            din[y] -= 1
            if din[y] == 0:
                q.enqueue(y)
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
    return (dist, p)

