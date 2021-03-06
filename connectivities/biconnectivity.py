# -*- coding: utf-8 -*-
"""
Undergraduate S4
Grahs: biconnectivity
"""

from algopy import graph
from algopy import stack


    
"""
first version: returns cut point vector and cut edge list
"""

def __cutpointsandedges(G, x, p, depth, cutPoints, cutEdges):
    """performs the DFS from x in G, returns the "higher (plushaut)" value of x
    
    :param p: x's parent
    :rtype: int
    """    
    ph_x = depth[x]
    for y in G.adjlists[x]:
        if depth[y] == -1:
            depth[y] = depth[x] + 1
            ph_y = __cutpointsandedges(G, y, x, depth, cutPoints, cutEdges)
            ph_x = min(ph_x, ph_y)
            if ph_y >= depth[x]:
                cutPoints[x] += 1
                if ph_y > depth[x]:
                    cutEdges.append((x, y))
        else:
            if y != p:
                ph_x = min(ph_x, depth[y])
            
    return ph_x
    
    
def cutpointsandedges(G):
    """ launches the DFS (first level here, next ones in recursive function)
        returns 
        - cut point vector (int list): how many times each vertex has been detected as cut point
        - cut edge list (int*int list)
    """    
    depth = [-1] * G.order    # mark vector: the depth in the spanning forest
    cutPoints = [0] * G.order
    cutEdges = []

    for x in range(G.order):
        if depth[x] == -1:    
            depth[x] = 0
            nbchildren = 0
            # the first level is done here
            for y in G.adjlists[x]:
                if depth[y] == -1:
                    nbchildren += 1
                    depth[y] = 1
                    ph_y = __cutpointsandedges(G, y, x, depth, cutPoints, cutEdges)
                    if ph_y > depth[x]:
                        cutEdges.append((x, y))

            cutPoints[x] = nbchildren - 1
    
    return (cutPoints, cutEdges)
    
"""
full version: returns previous function lists 
as well as the biconnected components ((int*int) list list)
"""
    
def __biconnectivity(G, x, p, depth, cutPoints, cutEdges, st, comp):
    """performs the DFS from x in G, returns the "higher (plushaut)" value of x
    
    :param p: x's parent
    :param st: edge stack
    :rtype: int
    """    
    ph_x = depth[x]
    for y in G.adjlists[x]:
        if depth[y] == -1:
            st.push((x, y))
            depth[y] = depth[x] + 1
            ph_y = __biconnectivity(G, y, x, depth, cutPoints, cutEdges, st, comp)
            ph_x = min(ph_x, ph_y)
            if ph_y >= depth[x]:
                cutPoints[x] += 1
                if ph_y > depth[x]:
                    cutEdges.append((x, y))
                bc = []
                x1 = -1
                while x1 != x:
                    (x1, y1) = st.pop()
                    bc.append((x1, y1))
                comp.append(bc)
        elif y != p and depth[y] < depth[x]:
            ph_x = min(ph_x, depth[y])
            st.push((x, y))
    return ph_x
    
    
def biconnectivity(G):
    depth = [-1] * G.order
    cutPoints = [0] * G.order
    cutEdges = []
    comp = []
    st = stack.Stack()
    for x in range(G.order):
        if depth[x] == -1:
            depth[x] = 0
            nbChildren = 0
            for y in G.adjlists[x]:
                if depth[y] == -1:
                    nbChildren += 1
                    st.push((x, y))
                    depth[y] = 1
                    ph_y = __biconnectivity(G, y, x, depth, cutPoints, cutEdges, st, comp)
                    if ph_y > 0:    # depth[x]
                        cutEdges.append((x, y))
                    bc = []
                    while not st.isempty():
                        bc.append(st.pop())
                    comp.append(bc)
                cutPoints[x] += nbChildren-1
    
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
    
    
    
