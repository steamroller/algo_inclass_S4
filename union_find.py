# -*- coding: utf-8 -*-
"""
Undergraduates - S4
Graphs connectivity:
Union-find algorithms and applications
Here graphs are given as pairs (order, edge list)
"""

from algopy.timing import timing

def __loadGRAasList(filename):
    f = open(filename)
    _ = bool(int(f.readline()))   # useless, always False!
    order = int(f.readline())
    L = []
    for line in f.readlines():
        edge = line.strip().split(' ')
        L.append((int(edge[0]), int(edge[1])))
    f.close()
    return (order, L)
    

# Union-Find
    
   
def find(x, p):
    while p[x] >= 0:
        x = p[x]
    return x

def union(x, y, p):
    rx = find(x, p)
    ry = find(y, p)
    if rx != ry:
        p[ry] = rx
        return True
    else:
        return False

#@timing
def buildUnionFind(n, L):
    '''
    n: integer > 0
    L: list of pairs (a, b) with a and b in [0, n[
    '''
    p = [-1]*n
    for (x, y) in L:
        union(x, y, p)
    return p


# optimized versions

def find2(x, p):
    rx = x
    while p[rx] >= 0:
        rx = p[rx]
        
    while p[x] >= 0:
        (p[x], x) = (rx, p[x])
        
    return rx

def union2(x, y, p):
    rx = find2(x, p)
    ry = find2(y, p)
    if rx != ry:
        if p[rx] < p[ry]:
            p[rx] = p[rx] + p[ry]
            p[ry] = rx
        else:
            p[ry] = p[ry] + p[rx]
            p[rx] = ry
        return True
    else:
        return False

#@timing
def buildUnionFind2(n, L):
    '''
    n: integer > 0
    L: list of pairs (a, b) with a and b in [0, n[
    '''
    p = [-1]*n
    for (x, y) in L:
        union2(x, y, p)
    return p

# applications

def makeMeConnected(n, L):
    """
    return the list of edges to add
    """
    p = buildUnionFind2(n, L)
    x = 0
    while p[x] >= 0:
        x += 1
    L = []
    for y in range(x+1, n):
        if p[y] < 0:
            L.append((x, y))
            # x = y
    return L



def makeComponentsUF(L, n):
    p = buildUnionFind2(n, L)
    cc = [None]*n
    k = 0
    for s in range(n)    :
        if p[s] < 0:
            k += 1
            cc[s] = k
    for s in range(n):
        cc[s] = cc[find2(s, p)]
    return (cc, k)
    
# TODO: find a better version     
    
    
    
def __nbVertexInComponentsUF(p):
    CCsizes = []
    for i in range(len(p)):
        if p[i] < 0:
            CCsizes.append(-p[i])
    return CCsizes

def Moon(n, L):
    p = buildUnionFind2(L, n)
    nbVert = __nbVertexInComponentsUF(p)
    k = len(nbVert)
    ways = 0
    for a in range(k):
        for b in range(a+1, k):
            ways += nbVert[a]*nbVert[b]
    return ways    
