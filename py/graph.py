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
        self.time = 0

    def visit(self, visit_fn, distance=0, time=0):
        self.visited = True
        self.distance = distance
        self.time = time
        visit_fn(self)


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
        """Breath first search starts from given node.  Use a queue to store
        to-visit nodes in order, in each round pop a node, visit it, visit its
        adjacent nodes, and add adjacent nodes to queue one by one, also update
        distance one by one
        """
        assert isinstance(node, GraphNode)
        q = [node]
        while len(q) > 0:
            src = q.pop(0)
            if not src.visited:
                src.visit(visit_fn)

            for dest in self.adjacent(src):
                if not dest.visited:
                    dest.visit(visit_fn, src.distance + 1)
                    q.append(dest)

    def dfs(self, node, visit_fn):
        """Depth first search starts from given node.  For given node and each
        of its adjacent node, do depth first search recursively
        """
        assert isinstance(node, GraphNode)

        # Make sure we start from the given node
        seq = [node]
        for x in self.nodes:
            if x is not node:
                seq.append(x)

        # Record visit time (sequence no.) when access each node.  We can define
        # a 'time = -1' and use 'nonlocal time' in _dfs_visit() but that won't
        # work with python 2.x, we here we use a tricky tip: when function
        # default arg is a list, the variable will become a static one.  We use
        # list 'time' for that purpose and only use time[0] to record the
        # sequence no.
        #
        def _dfs_visit(node, visit_fn, time=[-1]):
            """Depth first one node recursively"""
            # XXX: nonlocal time
            if not node.visited:
                time[0] = time[0] + 1
                node.visit(visit_fn, time=time[0])
            for x in self.adjacent(node):
                if not x.visited:
                    _dfs_visit(x, visit_fn)

        for src in seq:
            _dfs_visit(src, visit_fn)


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

    def visit_node_with_distance(node):
        assert isinstance(node, GraphNode)
        print 'Visiting graph node %s, distance is %d' % (node, node.distance)

    def visit_node_with_time(node):
        assert isinstance(node, GraphNode)
        print 'Visiting graph node %s, time is %d' % (node, node.time)

    print '\nBFS graph from node 0: (%s)' % graph[0]
    graph.clear_all()
    # Expect r, s, v, w, t, x, u, y
    graph.bfs(graph[0], visit_node_with_distance)

    print '\nDFS graph from node 0: (%s)' % graph[0]
    graph.clear_all()
    # Expect r, s, w, t, u, x, y, v
    graph.dfs(graph[0], visit_node_with_time)

# EOF
