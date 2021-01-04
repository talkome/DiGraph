from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def setUp(self) -> None:
        self.my_graph = DiGraph()
        for i in range(5):
            self.my_graph.add_node(i)

        self.my_graph.add_edge(0, 1, 3)
        self.my_graph.add_edge(0, 2, 1)
        self.my_graph.add_edge(2, 0, 9)
        self.my_graph.add_edge(1, 2, 20)
        self.my_graph.add_edge(1, 3, 5)
        self.my_graph.add_edge(1, 4, 7)
        self.my_graph.add_edge(3, 4, 55)
        self.my_graph.add_edge(4, 3, 34)

    def test_has_edge(self):
        self.assertTrue(self.my_graph.has_edge(0, 1))
        self.assertFalse(self.my_graph.has_edge(1, 0))
        self.assertFalse(self.my_graph.has_edge(3, 3))
        self.assertTrue(self.my_graph.has_edge(4, 3))

    def test_v_size(self):
        vertices = self.my_graph.get_all_v()
        self.assertEqual(len(vertices.keys()), self.my_graph.nodes_total)

    def test_e_size(self):
        self.my_graph.remove_edge(0, 2)
        self.assertEqual(7, self.my_graph.e_size())

    def test_get_all_v(self):
        self.assertEqual(self.my_graph.get_all_v().keys(), {0, 1, 2, 3, 4})

    def test_all_in_edges_of_node(self):
        self.assertEqual(self.my_graph.all_in_edges_of_node(0).keys(), {2})
        self.assertEqual(self.my_graph.all_in_edges_of_node(1).keys(), {0})
        self.assertEqual(self.my_graph.all_in_edges_of_node(2).keys(), {0, 1})
        self.assertEqual(self.my_graph.all_in_edges_of_node(3).keys(), {1, 4})
        self.assertEqual(self.my_graph.all_in_edges_of_node(4).keys(), {1, 3})

    def test_all_out_edges_of_node(self):
        self.assertEqual(self.my_graph.all_out_edges_of_node(0).keys(), {1, 2})
        self.assertEqual(self.my_graph.all_out_edges_of_node(1).keys(), {2, 3, 4})
        self.assertEqual(self.my_graph.all_out_edges_of_node(2).keys(), {0})
        self.assertEqual(self.my_graph.all_out_edges_of_node(3).keys(), {4})
        self.assertEqual(self.my_graph.all_out_edges_of_node(4).keys(), {3})

    def test_get_mc(self):  # TODO: fix
        self.g = DiGraph()
        for i in range(10):
            self.g.add_node(i)
        self.assertEqual(self.g.get_mc(), 10)

        for i in range(9):
            self.g.add_edge(i, i + 1, i + 1)
        self.assertEqual(self.g.get_mc(), 19)

        for i in range(6, 10):
            self.g.remove_node(i)
        self.assertEqual(self.g.get_mc(), 36)

    def test_add_edge(self):
        num_of_edges = self.my_graph.e_size()
        self.my_graph.add_edge(2, 4, 100)
        self.my_graph.remove_edge(2, 4)
        self.assertEqual(self.my_graph.e_size(), num_of_edges)
        self.assertFalse(self.my_graph.add_edge(11, 14, 55))

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
        self.my_graph.remove_node(1)
        self.assertEqual(4, self.my_graph.v_size())
        self.assertEqual(4, self.my_graph.e_size())

    def test_remove_edge(self):
        self.my_graph.remove_edge(0, 2)
        self.assertEqual(self.my_graph.e_size(), 7)
