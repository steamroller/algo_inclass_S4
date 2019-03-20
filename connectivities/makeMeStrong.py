# -*- coding: utf-8 -*-
"""
S4 - March 2019
Strong Connectivity Homework
"""

from algopy import graph
import strongConnectivity as scc


#------------------------------------------------------------------------------
def makeMeStrong_simple(G):
    """Makes G strongly connected
    Builds a circuit with one vertex per component
    """
    k, sccvect = scc.Tarjan(G)
    sccList = scc.from_scc2sccList(sccvect, k)
    
    x = sccList[0][0]
    for i in range(1, k):
        y = sccList[i][0]
        G.addedge(x, y)
        x = y
    G.addedge(x, sccList[0][0])

    
#------------------------------------------------------------------------------
    
def sourcesAndSinks(G):
    din = [0]*G.order
    sinks = []
    for s in range(G.order):
        for adj in G.adjlists[s]:
            din[adj] += 1
        if G.adjlists[s] == []:
            sinks.append(s)
    sources = []
    for s in range(G.order):
        if din[s] == 0:
            sources.append(s)
    return (sources, sinks)
    
      
def makeMeStronglyConnected(G):
    (Gr, comp) = scc.condenseGraph(G)
    nb = 0
    k = Gr.order
    if k > 1:
        (sources, sinks) = sourcesAndSinks(Gr)
        nb = len(sources) + len(sinks) - 1
     #vert[s] one vertex in G that belongs to component s in Gc        
        vert = [comp.index(i) for i in range(k)]        
        src = vert[sources[0]]
        x = src
        for i in range(1, len(sources)):
            y = vert[sources[i]]
            G.addedge(x, y)
            x = y
        s = vert[sinks[0]]
        for i in range(1, len(sinks)):
            s2 = vert[sinks[i]]
            G.addedge(s, s2)
            s = s2
        G.addedge(s, src)
    return nb
    
    
    
    
    
    
    
        
        
        
        