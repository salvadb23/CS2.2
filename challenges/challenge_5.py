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

    def DFS_recursive(self, v, v2):
        """searches the graph to see if there is a path between two vertices using DFS"""
        vertexObj = self.vertList[v]
        visited = {}
        visited[vertexObj.getId()] = True

        def dfs(vertex):
            visited[vertex.getId()] = True
            for neighbor in vertex.neighbors:
                if neighbor.getId() not in visited:
                    dfs(neighbor)
        dfs(vertexObj)
        path = list(visited.keys())
        end_path = path.index(v2) + 1

        is_path = v2 in path

        return (is_path, path[:end_path])

    def has_Eularian_Cycle(self):
        '''Test if a graph has an Eularian cycle i.e 
        returns True or False
        '''
        for vertex in self.vertList:
            if len(self.vertList[vertex].getNeighbors()) % 2 != 0:
                return False
        return True

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


def print_path_result(path, path_list):
    """prints result from eularian function above"""
    print("There exist a path between vertex {} and {}: {}".format(
        argv[2], argv[3], path))
    print('Vertices in path: {}'.format((',').join(path_list)))


if __name__ == "__main__":
    data = parse_data()
    g = create_graph(data)
    print(g.has_Eularian_Cycle())
