import unittest
from challenge_2 import Graph
from challenge_2 import Vertex


class GraphTest(unittest.TestCase):
    def test_shortest_path(self):
        g = Graph()
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addVertex(4)
        g.addVertex(5)

        g.addEdge(1, 2)
        g.addEdge(1, 4)
        g.addEdge(2, 3)
        g.addEdge(2, 4)
        g.addEdge(2, 5)
        g.addEdge(3, 5)

        self.assertEqual(3, len(g.shortest_path(1, 5)))


unittest.main()
