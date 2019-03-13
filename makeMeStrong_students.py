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
    #FIXME
    pass
    return (sources, sinks)
    
      
def makeMeStronglyConnected(G):
    (Gr, comp) = scc.condenseGraph(G)
    nb = 0 # nb added edges
    k = Gr.order
    if k > 1:
        (sources, sinks) = sourcesAndSinks(Gr)

     #vert[s] one vertex in G that belongs to component s in Gr        
        vert = [comp.index(i) for i in range(k)]        
        #FIXME
        pass



    return nb
    
    
    
    
    
    
    
        
        
        
        