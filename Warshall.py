# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:37:10 2017
@author: Nathalie
"""

from algopy import graph, matrices
from algopy.timing import timing

@timing
def Warshall(G):
    M = matrices.initMat(G.order, G.order, 0)
    for s in range(G.order):
#        M[s][s] = 1
        for adj in G.adjlists[s]:
            M[s][adj] = 1
            
    for k in range(G.order):
        for i in range(G.order):
            for j in range(G.order):
                M[i][j] = M[i][j] or M[i][k] and M[k][j]
    
    return M

# optimization?




def makeComponentsFromWarshall(M):
    #FIXME
    pass
    
    
    
    