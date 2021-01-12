import math

from src.GraphInterface import GraphInterface
from src.node_data import node_data

BLACK = 1
WHITE = 0
INFINITY = math.inf


class DiGraph(GraphInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.graph_vertices = dict()
        self.sons = dict()
        self.fathers = dict()
        self.vertices_total = 0
        self.edges_total = 0
        self.mc = 0

    def __iter__(self):
        return self.graph_vertices.values().__iter__()

    def __str__(self):
        return f"Graph: [MC:{self.mc}, Edges: {self.sons.values()}, Nodes: {self.graph_vertices.values()}]"

    def __repr__(self):
        return f"Graph: [MC:{self.mc}, Edges: {self.sons.items()}, Nodes: {self.graph_vertices.items()}]"

    def get_node(self, node_id: int) -> bool:
        """
        return true iff the graph contain this node
        @:param: node_id: node_data key
        @:return: true/false if there is edge between this two nodes
        """
        if node_id in self.graph_vertices.keys():
            return True
        else:
            return False

    def has_edge(self, src: int, dest: int) -> bool:
        """
        return true iff there is edge between this two nodes
        @:param: src: node_data 1 key
        @:param: dest: node_data 1 key
        @:return: true/false if there is edge between this two nodes
        """
        if src != dest and self.get_node(src) and self.get_node(dest):
            if dest in self.sons[src] and src in self.fathers[dest]:
                return True
        return False

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.vertices_total

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edges_total

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph,
        each node is represented using a pair  (key, node_data)
        """
        return self.graph_vertices

    def all_in_edges_of_node(self, node_id: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
        """
        return self.fathers[node_id]

    def all_out_edges_of_node(self, node_id: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id ,
        each node is represented using a pair (key,weight)
        """
        return self.sons[node_id]

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def clear(self):
        """
        this method clear the nodes information in the graph
        """
        vertices = self.get_all_v().values()
        for vertex in vertices:
            vertex.set_tag(WHITE)
            vertex.set_weight(INFINITY)
            vertex.set_info('')

    def add_edge(self, src: int, dest: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param src: The start node of the edge
        @param dest: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not
        exists the functions will do nothing
        """
        if not self.has_edge(src, dest) and self.get_node(src) and self.get_node(dest):
            self.sons[src][dest] = weight
            self.fathers[dest][src] = weight
            self.edges_total += 1
            self.mc += 1
            return True
        else:
            return False

    def remove_edge(self, src: int, dest: int) -> bool:
        """
         Removes an edge from the graph.
         @param src: The start node of the edge
         @param dest: The end node of the edge
         @return: True if the edge was removed successfully, False o.w.
         Note: If such an edge does not exists the function will do nothing
         """
        if self.has_edge(src, dest):
            del self.sons[src][dest]
            del self.fathers[dest][src]
            self.edges_total -= 1
            self.mc += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if not self.get_node(node_id):
            self.graph_vertices[node_id] = node_data(node_id, pos)
            self.sons[node_id] = {}
            self.fathers[node_id] = {}
            self.vertices_total += 1
            self.mc += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if self.get_node(node_id):
            self.edges_total -= len(self.sons[node_id])
            del self.sons[node_id]
            self.edges_total -= len(self.fathers[node_id])
            del self.fathers[node_id]
            self.graph_vertices.pop(node_id)
            self.vertices_total -= 1
            vertices = self.get_all_v()
            for vertex in vertices.keys():
                sons_list = self.all_out_edges_of_node(vertex)
                if node_id in sons_list.keys():
                    del self.sons[vertex][node_id]

                fathers_list = self.all_in_edges_of_node(vertex)
                if node_id in fathers_list.keys():
                    del self.fathers[vertex][node_id]

            self.mc += 1
            return True
        else:
            return False
