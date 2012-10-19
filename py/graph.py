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
    edge is expressed by its ending Vertex instance
    """

    def __init__(self, vertex, edges=None):
        assert isinstance(vertex, Vertex)
        self.vertex = vertex
        if edges:
            self.edges = edges
        else:
            self.edges = []
        self.clear()

    def __repr__(self):
        return '%s -> %s' % (self.vertex, self.edges)

    def clear(self):
        """Clear visited flag and reset distance"""
        self.visited = False
        self.distance = 0


class Graph(object):
    """A graph contains a list of grah nodes and a flag indicates whether it's a
    directed graph (digraph)
    """

    def __init__(self, digraph=False):
        self.digraph = digraph
        self.nodes = []

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        for x in self.nodes:
            yield x

    def __getitem__(self, n):
        return self.nodes[n]

    def add_node(self, node):
        """Add a GraphNode instance"""
        assert isinstance(node, GraphNode)
        self.nodes.append(node)

    def clear_all(self):
        """Clear all visited flag"""
        for node in self.nodes:
            node.clear()

    def adjacent(self, node):
        """Return a list of adjacent graph nodes (GraphNode) of given node"""
        out = []
        for v in node.edges:
            for x in self.nodes:
                if x.vertex == v:
                    out.append(x)
        return out

    def bfs(self, node, visit_fn):
        """Breath first search starts from node <node>.  Use a queue to store
        to-visit nodes in order, in each round pop a node, visit it, visit its
        adjacent nodes, and add adjacent nodes to queue one by one, also update
        distance one by one
        """
        assert isinstance(node, GraphNode)
        q = [node]
        while len(q) > 0:
            src = q.pop(0)
            visit_fn(src)
            for dest in self.adjacent(src):
                if not dest.visited:
                    dest.distance = src.distance + 1
                    visit_fn(dest)
                    q.append(dest)
            src.visited = True

    def dfs(self, n, visit_fn):
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

    def visit_node(node):
        assert isinstance(node, GraphNode)
        print 'Visiting graph node %s, distance is %d' % (node, node.distance)

    print 'BFS graph from node 0: (%s)' % graph[0]
    graph.clear_all()
    graph.bfs(graph[0], visit_node)

    print 'DFS graph from node 0: (%s)' % graph[0]
    graph.clear_all()
    graph.dfs(graph[0], visit_node)

# EOF
