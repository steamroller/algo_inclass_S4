# -*- coding: utf-8 -*-
"""
Graphs: puzzles
Coloration: simple algorithms
"""

from algopy import graph


def __testColor(G, colors):
    for s in range(G.order):
        for adj in G.adjlists[s]:
            if colors[s] == colors[adj]:
                print(s, adj)
                return False
    return True
    
def __degrees(G):
    d = [0]*G.order
    for s in range(G.order):
        d[s] = (len(G.adjlists[s]), s)
    return d


# greedy algorithm

def colorgreedy(G):
    colors = [None] * G.order
    colors[0] = 1
    nb = 1
    for s in range(1, G.order):
        col = [0] * (nb+1)
        for adj in G.adjlists[s]:
            if colors[adj]:
                col[colors[adj]] += 1
        i = 1
        while i < nb+1 and col[i] != 0:
            i += 1
        colors[s] = i
        nb = max(nb, i)
    return nb, colors
        
    
    
    
# Welsh-Powell algorithm
def Welsh_Powell(G):
    deg = __degrees(G)
    deg.sort(reverse=True)
    colors = [0] * G.order
    col = 1
    nb = 0
    for (_, s) in deg:
        if colors[s] == 0:
            colors[s] = col
            L = G.adjlists[s]
            nb += 1
            for notAdj in range(G.order):
                if colors[notAdj] == 0 and (notAdj not in L):
                    colors[notAdj] = col
                    L = L + G.adjlists[notAdj]
            col += 1
    return (col-1, colors)

