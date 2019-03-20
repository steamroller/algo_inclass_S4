# -*- coding: utf-8 -*-
"""
A* implementation with heaps
"""

from algopy import graph
from algopy import heap_spe as heap

inf = float('inf')


# basic version: assume that dst is reachable from src
# "bonus" -> Exception if dst is not reachable from src: 1 point!

def astar(G, src, dst, heur):
    """
        heur: heuristix (vector)
        prints the list of processed vertices
        returns, as usual, dist and p
    """

    #FIXME
    pass
    
    print("Processed vertices:", processed)
    return (dist, p)



    
# tests: search shortest path from 0 to 9
G = graph.load_weightedgraph("files/digraph_astar.wgra", int)
heuristixD = [0] * 10
heuristixM = [3, 2, 3, 1, 1, 5, 4, 3, 2, 0]
heuristixB = [0, 9, 1, 1, 3, 2, 2, 1, 1, 2] 
# add-on (in tutorial)
H = [3, 2, 3, 1, 3, 6, 4, 3, 2, 0]

