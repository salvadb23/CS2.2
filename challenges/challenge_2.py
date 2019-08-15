#!python

"""
Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from sys import argv


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if (vertex not in self.neighbors):
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        return self.neighbors[vertex]


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def __str__(self):
        for item in self.vertList:
            print(item)
        return 'done'

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self, vertex):
        """return the vertex if it exists"""
        return self.vertList[vertex] if self.vertList[vertex] is not None else False

    def addEdge(self, vertexOne, vertexTwo, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if self.vertList[vertexOne] is None:
            self.addVertex(vertexOne)
        elif self.vertList[vertexTwo] is None:
            self.addVertex(vertexTwo)
        else:
            self.vertList[vertexOne].addNeighbor(
                self.vertList[vertexTwo], cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def shortest_path(self, vertex_one, vertex_two):
        """searches the graph and returns the nodes at n level depth"""
        queue = [(vertex_one, 0)]
        visited = {}
        path = []
        while queue:
            if vertex_two in visited:
                break
            vertex, parent = queue.pop(0)
            if len(visited.keys()) is len(self.vertList):
                break
            if vertex not in visited:
                visited[vertex] = parent

            for neighbor in self.vertList[vertex].neighbors:
                if neighbor not in visited:
                    queue.append((neighbor.getId(), vertex))

        child = vertex_two
        while vertex_one not in path:
            path.append(child)
            child = visited[child]
        return path[::-1]

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


def parse_data():
    """reads file from command line"""
    vertices = open(argv[1], 'r')
    graph_data = vertices.read().split()
    vertices.close()
    return graph_data


def create_graph(graph_data):
    """Create a graph from an array of graph information"""
    is_graph = graph_data[0] is 'G'

    graph = Graph()

    for vertex in graph_data[1].split(','):
        graph.addVertex(vertex)

    counter = 0

    for word in graph_data[2:]:
        counter += 1
        if is_graph:
            graph.addEdge(word[3], word[1],
                          word[5:].replace(')', ''))
            graph.addEdge(word[1], word[3],
                          word[5:].replace(')', ''))
        else:
            graph.addEdge(word[1], word[3],
                          word[5:].replace(')', ''))

    return graph


def print_shortest_path(graph):
    """prints the shortest path"""
    path = graph.shortest_path(argv[2], argv[3])
    for key in path:
        print(key, end=',')
    print('\nNumber of edges in shortest path: {}'.format(len(path)-1))


if __name__ == "__main__":
    print_shortest_path(create_graph(parse_data()))
