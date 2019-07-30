import unittest
from challenge_1 import Graph
from challenge_1 import Vertex

class GraphTest(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.addVertex(1)
        g.addVertex(2)

        self.assertEqual(2, len(g.getVertices()))

unittest.main()