# -*- coding: utf-8 -*-
"""
S4 - 2019-02
Strong Connectivity
"""

from algopy import graph, stack


#------------------------------------------------------------------------------
# tools

def reverseGraph(G):
    G_1 = graph.Graph(G.order, True)
    for s in range(G.order):
        for adj in G.adjlists[s]:
            G_1.addedge(adj, s)
    return G_1

def from_scc2sccList(comp, nb):
    c = []
    for i in range(nb):
        c.append([])
    for i in range(len(comp)):
        c[comp[i]-1].append(i)
    return c

def from_sccList2scc(sccList, n):
    k = len(sccList)
    scc = [-1] * n
    for i in range(k):
        for s in sccList[i]:
            scc[s] = i
    return k, scc

#------------------------------------------------------------------------------
# 2.1 naive 
def __dfs(G, s, M, mark = True):
    M[s] = mark
    for adj in G.adjlists[s]:
        if not M[adj]:
            __dfs(G, adj, M, mark)

def simpleDFS(G, s):
    M = [False]*G.order
    __dfs(G, s, M)
    return M
    
def naiveAlgo(G):
    G_1 = reverseGraph(G)
    comp = [0]*G.order
    no = 0
    for x in range(G.order):
        if comp[x] == 0:
            plus = simpleDFS(G, x)
            minus = simpleDFS(G_1, x)
            no += 1
            for y in range(G.order):
                if plus[y] and minus[y]:
                    comp[y] = no
    return (no, comp)


#------------------------------------------------------------------------------
# 2.2 Kosaraju


def __dfsPost(G, s, M, post):
    M[s] = True
    for adj in G.adjlists[s]:
        if not M[adj]:
            __dfsPost(G, adj, M, post)
    post.push(s)

def Kosaraju(G):
    post = stack.Stack()
    M = [False]*G.order
    for s in range(G.order):
        if not M[s]:
            __dfsPost(G, s, M, post)
    
    G_1 = reverseGraph(G)
    comp = [0]*G.order
    no = 0
    while not post.isEmpty():
        s = post.pop()
        if comp[s] == 0:
            no += 1
            __dfs(G_1, s, comp, no)
    
    return (no, comp)


#------------------------------------------------------------------------------
# 2.2 Tarjan

def __Tarjan(G, x, pref, cpt, cfc, nocfc, vertexStack):
    cpt += 1
    pref[x] = cpt
    return_x = pref[x]
    vertexStack.push(x)
    for y in G.adjlists[x]:
        if pref[y] == 0:
            (return_y, cpt, nocfc) = __Tarjan(G, y, pref, cpt, cfc, nocfc, vertexStack)
            return_x = min(return_x, return_y)
        else:
            return_x = min(return_x, pref[y])
    if return_x == pref[x]:
        nocfc += 1           
        y = -4
        while y != x:
            y = vertexStack.pop()
            cfc[y] = nocfc
            pref[y] = 4 * G.order
            
    return (return_x, cpt, nocfc)


def Tarjan(G):
    pref = [0]*G.order
    cpt = 0
    vertexStack = stack.Stack()
    k = 0
    cfc = [0]*G.order
    for s in range(G.order):
        if pref[s] == 0:
            (_, cpt, k) = __Tarjan(G, s, pref, cpt, cfc, k, vertexStack)
    return (k, cfc )

