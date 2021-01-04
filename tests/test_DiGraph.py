from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def setUp(self) -> None:
        self.my_graph = DiGraph()
        for i in range(6):
            self.my_graph.add_node(i)

        self.my_graph.add_edge(0, 1, 3)
        self.my_graph.add_edge(0, 2, 1)
        self.my_graph.add_edge(1, 2, 20)
        self.my_graph.add_edge(1, 3, 5)
        self.my_graph.add_edge(1, 4, 7)

    def test_has_edge(self):
        pass

    def test_v_size(self):
        vertices = self.my_graph.get_all_v()
        self.assertEqual(vertices.__sizeof__(), self.my_graph.nodes_total)

    def test_e_size(self):
        self.my_graph.remove_edge(0, 2)
        self.assertEqual(4, self.my_graph.e_size())

    def test_get_all_v(self):
        pass

    def test_all_in_edges_of_node(self):
        pass

    def test_all_out_edges_of_node(self):
        pass

    def test_get_mc(self):
        pass

    def test_add_edge(self):
        num_of_edges = self.my_graph.edges_total
        self.my_graph.add_edge(2, 4, 100)
        self.my_graph.remove_edge(2, 4)
        self.assertEqual(self.my_graph.edges_total, num_of_edges)
        self.my_graph.add_edge(11, 14, 55)

    def test_add_node(self):
        first_mc = self.my_graph.get_mc()
        num_of_nodes = self.my_graph.v_size()
        self.my_graph.add_node(2)
        self.assertEqual(first_mc, self.my_graph.get_mc())
        self.assertEqual(num_of_nodes, self.my_graph.v_size())
        self.my_graph.add_node(6)
        self.assertEqual(first_mc + 1, self.my_graph.get_mc())
        self.assertEqual(num_of_nodes + 1, self.my_graph.v_size())

    def test_remove_node(self):
        num_of_nodes = self.my_graph.nodes_total
        num_of_edges = self.my_graph.edges_total
        self.my_graph.remove_node(1)
        self.assertEqual(num_of_nodes - 1, self.my_graph.nodes_total)
        self.assertEqual(num_of_edges - 4, self.my_graph.edges_total)

    def test_remove_edge(self):
        pass
