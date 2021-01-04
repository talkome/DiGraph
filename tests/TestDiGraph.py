from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.my_graph = None

    def setUp(self) -> None:
        my_graph = DiGraph()
        for i in range(6):
            my_graph.add_node(i)
        my_graph.add_edge(0, 1, 3)
        my_graph.add_edge(1, 2, 1)
        my_graph.add_edge(2, 0, 20)
        my_graph.add_edge(1, 3, 5)
        my_graph.add_edge(1, 4, 7)

    def tests(self):
        # print("graph:", self.my_graph.graph_node.keys())
        self.my_graph.remove_edge(2, 0)
        num_of_edges = 4
        num_of_nodes = 5
        self.assertEqual(num_of_edges, self.my_graph.e_size)
        self.assertEqual(num_of_nodes, self.my_graph.v_size)

        self.my_graph.remove_edge(1, 2)
        num_of_edges = 3
        self.assertEqual(num_of_edges, self.my_graph.e_size)
        self.my_graph.remove_node(2)
        num_of_nodes = 4
        self.assertEqual(num_of_nodes, self.my_graph.v_size)
        print("graph:", self.my_graph.graph_node.keys())

        print("sons:", self.my_graph.sons.keys())
        print("fathers:", self.my_graph.fathers.keys())
        self.my_graph.add_edge(0, 3, 4)
        print("sons:", self.my_graph.sons.keys())
        print("fathers:", self.my_graph.fathers.keys())
        self.my_graph.remove_edge(0, 1)
        print("remove edge (0,1)")
        print("sons:", self.my_graph.sons.keys())
        print("fathers:", self.my_graph.fathers.keys())
        print(self.my_graph.graph_node.keys())
