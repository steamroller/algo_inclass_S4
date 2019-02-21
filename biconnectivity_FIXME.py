# -*- coding: utf-8 -*-
"""
Undergraduate S4
Grahs: biconnectivity
Student's
"""

from algopy import graph
from algopy import stack


    
def __biconnectivity(G, x, p, depth, cutPoints, cutEdges, st, comp):
    """performs the DFS from x in G, returns the "higher (plushaut)" value of x
    
    :param p: x's parent
    :param st: edge stack
    :rtype: int
    """    
    ph_x = depth[x]
    for y in G.adjlists[x]:
        if depth[y] == -1:

            depth[y] = depth[x] + 1
            ph_y = __biconnectivity(G, y, x, depth, cutPoints, cutEdges, st, comp)












        else:


    return ph_x
    
    
def biconnectivity(G):
    """ launches the DFS (first level here, next ones in recursive function)
        returns 
        - cut point vector (int list): how many times each vertex has been detected as cut point
        - cut edge list (int*int list)
        - biconnected components ((int*int) list list)
    """    

    depth = [-1] * G.order
    cutPoints = [0] * G.order
    cutEdges = []
    comp = []
    st = stack.Stack()
    for x in range(G.order):
        if depth[x] == -1:
            depth[x] = 0
     
        
            for y in G.adjlists[x]:
                if depth[y] == -1:
        


                    depth[y] = 1
                    ph_y = __biconnectivity(G, y, x, depth, cutPoints, cutEdges, st, comp)











    
    return (cutPoints, cutEdges, comp)
    
    
# results with "files/graphISP_2.gra"
    
cutPoints, cutEdges = ([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2], 
                       [(9, 12), (13, 11), (0, 13)])
    
comp = [[(6, 5), (6, 0), (2, 6), (5, 2), (0, 5)],
  [(10, 13), (8, 3), (8, 1), (10, 8), (7, 10), (1, 7), (3, 1), (13, 3)],
  [(9, 12)],
  [(9, 11), (4, 9), (11, 4)],
  [(13, 11)],
  [(0, 13)]]  
    
    
    
