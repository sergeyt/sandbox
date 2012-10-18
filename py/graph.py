#!/usr/bin/env python

"""To demo graph algorithms"""


class Vertex(object):
    """A vertex contains a char as its information"""

    def __init__(self, char):
        self.info = char

    def __repr__(self):
        return self.info


class GraphNode(object):
    """A graph node contains a Vertex instance and all its adjacent edges, an
    edge is expressed by a Vertex instance
    """

    def __init__(self, vertex, edges=None):
        assert isinstance(vertex, Vertex)
        self.vertex = vertex
        if edges:
            self.edges = edges
        else:
            self.edges = []
        self.__visited = False

    def __repr__(self):
        return '%s -> %s' % (self.vertex, self.edges)

    def visited(self):
        return self.__visited

    def clear(self):
        """Clear visited flag"""
        self.__visited = False


class Graph(object):
    """A graph contains a set of grah nodes"""

    def __init__(self, digraph=False):
        self.digraph = digraph
        self.nodes = []

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        for x in self.nodes:
            yield x

    def add_node(self, node):
        """Add a GraphNode instance"""
        assert isinstance(node, GraphNode)
        self.nodes.append(node)

    def clear_all(self):
        """Clear all visited flag"""
        for node in self.nodes:
            node.clear()

    def bfs(self, n):
        """Breath first search starts fro nodes[n]"""
        pass

    def dfs(self, n):
        """Depth first search starts fro nodes[n]"""
        pass


if __name__ == '__main__':
    """Example graph (page 596):

        r - s   t - u
        |   | / | / |
        v   w - x - y

    """

    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')

    graph = Graph()
    graph.add_node(GraphNode(r, [s, v]))
    graph.add_node(GraphNode(s, [r, w]))
    graph.add_node(GraphNode(t, [u, w, x]))
    graph.add_node(GraphNode(u, [t, x, y]))
    graph.add_node(GraphNode(v, [r]))
    graph.add_node(GraphNode(w, [s, t, x]))
    graph.add_node(GraphNode(x, [t, w, y]))
    graph.add_node(GraphNode(y, [u, x]))

    print 'Graph has %d nodes' % len(graph)
    for n in graph:
        print n

    print 'BFS graph from node 0: (%s)' % graph.nodes[0]
    graph.clear_all()
    print graph.bfs(0)

    print 'DFS graph from node 0: (%s)' % graph.nodes[0]
    graph.clear_all()
    print graph.dfs(0)

# EOF
