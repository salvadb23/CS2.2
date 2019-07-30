from challenge_3 import Graph
from challenge_3 import Vertex
import unittest


class GraphTest(unittest.TestCase):
    def test_shortest_path(self):
        g = Graph()
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addVertex(4)
        g.addVertex(5)

        g.addEdge(1,2)
        g.addEdge(1,4)
        g.addEdge(2,3)
        g.addEdge(2,4)
        g.addEdge(2,5)
        g.addEdge(3,5)

        is_path, path = g.DFS_recursive(1,5)

        self.assertEqual(4,len(path))

unittest.main()