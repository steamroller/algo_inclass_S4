# -*- coding: utf-8 -*-
"""Graph module.

Provide an implementation of graphs with adjacency lists.

In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. The vertex key, or number, can then be used to access its
adjacency list.

"""


class Graph:
    """ Simple class for graph: adjacency lists

    Attributes:
        order (int): Number of nodes.
        directed (bool): True if the graph is directed. False otherwise.
        adjlists (List[List[int]]): Lists of connected vertices for each vertex.

    """

    def __init__(self, order, directed=False, labels=None, costs=False):
        """Init graph, allocate adjacency lists

        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.
            costs (bool): True if the graph is weighted. False otherwise. 

        """

        self.order = order
        self.directed = directed
        if costs:
            self.costs = {}
        else:
            self.costs = None
        self.adjlists = []
        for _ in range(order):
            self.adjlists.append([])
        self.labels = labels


    def addedge(self, src, dst, cost=None, multi=True):
        """Add egde to graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
            cost: if not None, the cost of edge (src, dst)
            multi (bool): True for multigraphs
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
    
        # Check graph and vertex indices.
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        if multi or (src != dst and dst not in self.adjlists[src]):
            self.adjlists[src].append(dst)
            if not self.directed and dst != src:
                self.adjlists[dst].append(src)
        if self.costs != None:
            self.costs[(src, dst)] = cost
            if not self.directed:
                self.costs[(dst, src)] = cost


    def addvertex(self, number=1):
        """Add number vertices to graph.
    
        Args:
            ref (Graph).
            number (int): Number of vertices to add.
    
        Raises:
            Exception: If graph is None.
    
        """
    
        # Check graph
        if self is None:
            raise Exception('Empty graph')
        # Increment order and extend adjacency list
        self.order += number
        for _ in range(number):
            self.adjlists.append([])

    def removeedge(self, src, dst):
        """Remove egde from the graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
    
        # Check graph and vertex indices.
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        if dst in self.adjlists[src]:
            self.adjlists[src].remove(dst)
            if self.costs:
                self.costs.pop((src, dst))
            if not self.directed and dst != src:
                self.adjlists[dst].remove(src)
                if self.costs:
                    self.costs.pop((dst, src))
                
        
def todot(ref):
    """Write down dot format of graph.

    Args:
        ref (Graph).

    Returns:
        str: String storing dot format of graph.

    """

    # Check if empty graph.
    if ref is None:
        return "graph G { }"
    # Build dot for non-empty graph.
    (s, link) = ("digraph ", " -> ") if ref.directed else ("graph ", " -- ")
    s += " G {\n"
    s += "node [shape = circle]\n"
    for src in range(ref.order):
        if ref.labels:
            s += "  " + str(src) + '[label = "' + ref.labels[src] + '"]\n'
        else:
            s += "  " + str(src) + '\n'        
        for dst in ref.adjlists[src]:
            cost = ' [label=' + str(ref.costs[(src, dst)]) + '] ' if ref.costs else ""
            if ref.directed or src >= dst:
                s += "  " + str(src) + link + str(dst) + cost + '\n'
    s += '}'
    return s

def toDotHighlightEdges(G, edges):
    (dot, link) = ("digraph ", " -> ") if G.directed else ("graph ", " -- ")
    dot += "G {\n"
    dot += "node [shape = circle]\n"
    #vertex traversal
    
    for s in range(G.order):
        if G.labels:
            dot += "  " + str(s) + '[caption = "' + G.labels[s] + '"]\n'
        else:
            dot += "  " + str(s) + '\n'        
        # adjacent list traversal
        for adj in G.adjlists[s]:   
            if G.directed or s >= adj:
                if (s, adj) in edges or (adj, s) in edges:
                    highLight = ', color="red", style="bold"'
                else:
                    highLight = ''
                cost = 'label=' + str(G.costs[(s, adj)]) if G.costs else ''
                if highLight or cost:
                    cost = ' [' + cost + highLight + ']'
                dot += "  " + str(s) + link + str(adj) + cost + '\n'
    dot += '}'
    return dot
    



def display(ref, eng=None, highlightedges=None):
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    if highlightedges:
        dot = toDotHighlightEdges(ref, highlightedges)
    else:
        dot = todot(ref)
    display(Source(dot, engine = eng))

    
# load / save gra(wgra) format    

def loadgra(filename, multigraph=True):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist. ????

    """

    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]:
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    g = Graph(order, directed)
    g.infos = infos
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (src, dst) = (int(edge[0]), int(edge[1]))
        g.addedge(src, dst, multi=multigraph)
    f.close()
    return g



def load_weightedgraph(filename, costType=float):
    """Build a new weighted graph from a WGRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.
    """
    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]:
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    G = Graph(order, directed, costs=True)
    G.infos = infos
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (x, y, cost) = (int(edge[0]), int(edge[1]), costType(edge[2]))
        G.addedge(x, y, cost)
    f.close()

    return G
    
def savegra(G, fileOut):
    gra = str(int(G.directed)) + '\n'
    gra += str(G.order) + '\n'
    for s in range(G.order):
        for adj in G.adjlists[s]:
            if G.directed or s >= adj:
                gra += str(s) + " " + str(adj) + '\n'
    fout = open(fileOut, mode='w')
    fout.write(gra)
    fout.close()


# add-on: sorts adjacency lists -> to have same results as those asked in tutorials/exams

def sortgraph(G):
    for i in range(G.order):
        G.adjlists[i].sort()

#
def fromlist(order, directed, edges):
    """Build a new graph from an int tuple list.

    Args:
        order (int): Order of graph.
        directed (bool): True if the graph is directed. False otherwise.
        edges (List[(int, int)]): Source/Destination tuple list.

    Returns:
        Graph: New graph.

    Raises:
        IndexError: If either order or edge extremity is invalid.

    """

    # Check order:
    if order <= 0:
        raise IndexError('Invalid order')
    # Build graph
    g = Graph(order, directed)
    for (src, dst) in edges:
        g.addedge(src, dst)
    return g

# Another way to display graphs

def displaySVG(ref, filename='temp'):
    """Render a graph to SVG format.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (Graph).
        filename (str): Temporary filename to store SVG output.

    Returns:
        SVG: IPython SVG wrapper object for graph.

    """

    # Ensure all modules are available
    try:
        from graphviz import Graph as gvGraph, Digraph as gvDigraph
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse graph and generate temporary Digraph/Graph object
    output_format = 'svg'
    if ref.directed:
        graph = gvDigraph(filename, format=output_format)
    else:
        graph = gvGraph(filename, format=output_format)
    if ref is not None:
        for src in range(ref.order):
            src_id = 'node_' + str(src)
            graph.node(src_id, label=str(src))
            for dst in ref.adjlists[src]:
                if ref.directed or src >= dst:
                    graph.edge(src_id, 'node_' + str(dst))
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)

