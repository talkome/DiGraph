import json
import math
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface

BLACK = 1
WHITE = 0
INFINITY = math.inf


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self, graph=DiGraph()):
        self.graph = graph

    def get_graph(self) -> DiGraph:
        """
        return the directed graph on which the algorithm works on.
        :@return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name) as file:
                load_file = json.load(file)
                load_graph = DiGraph()
            for vertex in load_file["Nodes"]:
                if vertex["pos"] is None:
                    load_graph.add_node(vertex["id"])
                else:
                    pos = tuple(map(float, vertex["pos"][1:-1].split(',')))
                    load_graph.add_node(vertex["id"], pos)

            for edge in load_file["Edges"]:
                load_graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = load_graph
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            file.close()

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        with open(file_name, 'w+') as file:
            try:
                result = {"Edges": [], "Nodes": []}
                for src_node in self.graph.sons.keys():
                    for dest_node, weight in self.graph.all_out_edges_of_node(src_node).items():
                        result["Edges"].append({'src': src_node, 'w': weight, 'dest': dest_node})

                for src_node in self.graph.get_all_v().values():
                    if src_node.get_pos() is None:
                        result["Nodes"].append({'pos': str((0, 0, 0)), "id": src_node.get_key()})
                    else:
                        result["Nodes"].append({'pos': str(src_node.get_pos()), 'id': src_node.get_key()})
                json.dump(result, ensure_ascii=False, indent=4, fp=file)
                return True
            except Exception as ex:
                print("couldn't save to jason: ", ex.__repr__())
                return False
            finally:
                file.close()

    def shortest_path(self, src: int, dest: int) -> (float, list):
        """
        returns the shortest path from node id1 to node
        id2 using Dijkstra's Algorithm
        @param src: The start node id
        @param dest: The end node id
        @return: The distance of the path, the path as a list
        """
        result = []
        vertices = self.graph.get_all_v()
        if self.graph.v_size() == 0 or not self.graph.get_node(src) or not self.graph.get_node(dest):
            return None
        if src == dest or self.graph.v_size() == 1:
            result.append(src)
            return result

        self.dijkstra(src)
        dest_node = vertices[dest]
        dest_str = dest_node.get_info()
        if dest_str == '':
            return None
        str_arr = dest_str.split('->')
        for s in str_arr:
            if s.isnumeric():
                new_node = vertices[int(s)]
                result.append(new_node.get_key())
        result.append(dest_node.get_key())
        result.sort(key=lambda x: x.key, reverse=False)
        return dest_node.get_weight(), result

    def connected_component(self, node_id: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param node_id: The node id
        @return: The list of nodes in the SCC
        """
        result = self.connected_components()
        for node_list in result:
            if node_id in node_list:
                return node_list

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        Complexity: O(|V|+|E|)
        @return: The list all SCC
        """
        result = []
        stack = []
        self.graph.clear()
        vertices = self.graph.get_all_v().values()
        for vertex in vertices:
            if vertex.get_tag() == WHITE:
                self.dfs(vertex.get_key(), stack)

        self.graph.clear()
        stack.reverse()
        while stack:
            curr_node = stack.pop()
            if curr_node.get_tag() == WHITE:
                scc = []
                self.dfs_t(curr_node.get_key(), scc)
                result.append(scc)
        return result

    def plot_graph(self) -> None:  # TODO: finish
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        pass

    def dfs(self, src, stack):
        """
        an algorithm for traversing or searching tree or graph data1 structures.
        it starts at the given node in the graph,
        and explores all of the connected nodes is the nodes component
        @ param source the node from which the search will start.
        """
        vertices = self.graph.get_all_v()
        curr_node = vertices[src]
        curr_node.set_tag(BLACK)
        stack.append(curr_node)

        sons_list = self.graph.all_out_edges_of_node(curr_node.get_key())
        for son in sons_list:
            vertex = vertices[son]
            if vertex.get_tag() == WHITE:
                self.dfs(vertex.get_key(), stack)

    def dfs_t(self, src, stack):
        """
         an algorithm for traversing or searching tree or graph data1 structures.
         it starts at the given node in the graph,
         and explores all of the connected nodes is the nodes component
         @ param source the node from which the search will start.
         """
        vertices = self.graph.get_all_v()
        curr_node = vertices[src]
        curr_node.set_tag(BLACK)
        stack.append(curr_node.get_key())

        sons_list = self.graph.all_in_edges_of_node(curr_node.get_key())
        for vertex in sons_list:
            son = vertices[vertex]
            if son.get_tag() == WHITE:
                self.dfs_t(son.get_key(), stack)

    def dijkstra(self, src):
        """
        Put the given vertex in the priority queue,
        priority queue sort the vertices by they tags value
        for each vertex we sum the current vertex's tag with his connected edge's weight
        each time we poll vertex with the minimal value in the priority queue
        go over all its neighbors, select the neighbor with the minimal value and put it in the priority queue
        mark all the vertex we passed,
        if there is a path with a minimal weight we will discover it and select this path
        each vertex we finished passing out of the priority queue
        @param src - The vertex we put in the priority queue
        """
        self.graph.clear()
        priority_queue = []
        vertices = self.graph.get_all_v()
        start_node = vertices[src]
        start_node.set_tag(WHITE)
        start_node.set_weight(0)
        priority_queue.append(start_node)

        while priority_queue:
            priority_queue.sort(key=lambda x: x.weight, reverse=False)
            curr_node = priority_queue.pop()
            curr_node_weight = curr_node.get_weight()
            if curr_node.get_tag() == WHITE:
                sons_list = self.graph.all_out_edges_of_node(curr_node.get_key()).items()
                for vertex, weight in sons_list:
                    son = vertices[vertex]
                    edge_weight = weight
                    if curr_node_weight + edge_weight < son.get_weight():
                        son.set_weight(curr_node_weight + edge_weight)
                        key = str(curr_node.get_info())
                        key += '->'
                        key += str(curr_node.get_key())
                        son.set_info(info=key)
                        if son.get_tag() == WHITE:
                            priority_queue.append(son)
                curr_node.set_tag(BLACK)


g1 = GraphAlgo()
for node in range(5):
    g1.graph.add_node(node)

g1.graph.add_edge(1, 0, 1)
g1.graph.add_edge(0, 2, 4)
g1.graph.add_edge(2, 1, 11)
g1.graph.add_edge(0, 3, 7)
g1.graph.add_edge(3, 4, 5)

ans = g1.connected_components()
print(ans)  # [[0, 1, 2], [3], [4]]
ans = g1.connected_component(0)
print(ans)  # [0, 1, 2]
