# -*- coding: utf-8 -*-
"""
Feb. 2019
Connected Graphs and connected components with dfs
@author: Nathalie
"""

from algopy import graph, graphmat

# to test on large graphs
import sys
sys.setrecursionlimit(3000)

#------------------------------------------------------------------------------

# test: graph is connected?

def __nbVertexDFS(G, s, M):
    M[s] = True
    nb = 1
    for adj in G.adjlists[s]:
        if not M[adj]:
            nb += __nbVertexDFS(G, adj, M)
    return nb
    
def isConnected(G):
    M = [False]*G.order
    return __nbVertexDFS(G, 0, M) == G.order

#------------------------------------------------------------------------------
# Indicateurs de connexité (connectivity indicators?)
    
def connectivity(G):
    M = [False]*G.order
    k = 0
    IC2 = 0
    for s in range(G.order):
        if not M[s]:
            k += 1
            nb = __nbVertexDFS(G, s, M)
            IC2 += nb*nb
    IC1 = (G.order - k) / (G.order-1)
    IC2 = IC2 / (G.order * G.order)
    return (IC1, IC2)

#------------------------------------------------------------------------------
# find connected components: basic...

def __components(G, s, cc, no):
    cc[s] = no
    for adj in G.adjlists[s]:
        if cc[adj] == 0:
            __components(G, adj, cc, no)

def components(G):
    '''
    return (nbc, cc)
    nbc: the number of connected components
    cc: the vector of components (cc[i] is the number of the component i belongs to)
    '''
    
    cc = [0]*G.order
    no = 0
    for s in range(G.order):
        if cc[s] == 0:
            no += 1
            __components(G, s, cc, no)
    return (no, cc)

def component_list(G):
    '''
    return the list of G's connected components: 
    each component is a list of vertices
    '''
    k, cc = components(G)
    L = [[] for _ in range(k)]
    for i in range(G.order):
        L[cc[i]-1].append(i)
    return L






    

        
