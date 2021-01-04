from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def setUp(self) -> None:
        self.g_algo = GraphAlgo()
        for i in range(10):
            self.g_algo.graph.add_node(i)

        self.g_algo.graph.add_edge(0, 1, 3)
        self.g_algo.graph.add_edge(0, 2, 9)
        self.g_algo.graph.add_edge(1, 2, 7)
        self.g_algo.graph.add_edge(1, 3, 5)
        self.g_algo.graph.add_edge(1, 4, 22.2)
        self.g_algo.graph.add_edge(3, 4, 12)
        self.g_algo.graph.add_edge(5, 4, 11)
        self.g_algo.graph.add_edge(6, 4, 7)
        self.g_algo.graph.add_edge(7, 3, 8)
        self.g_algo.graph.add_edge(8, 2, 10)

    def test_shortest_path(self):
        self.assertEqual(self.g_algo.shortest_path(1, 4), (17, [1, 3, 4]))
        self.assertEqual(self.g_algo.shortest_path(0, 3), (8, [0, 1, 3]))
        self.assertEqual(self.g_algo.shortest_path(0, 4), (20, [0, 1, 3, 4]))
        self.assertIsNone(self.g_algo.shortest_path(0, 7))

    def test_connected_component(self):
        # actual = [[0, 1, 2], [7], [3], [4], [6], [5], [8]]
        self.assertEqual(self.g_algo.connected_components(), [[0], [1], [2, 8], [3, 7], [4, 5, 6], [9]])

    def test_connected_components(self):
        ans = self.g_algo.connected_component(0)
        self.assertEqual(ans, [[0, 1, 2]])

    # def test_plot_graph(self):
    #     pass

    def test_save_load_from_json(self):
        self.assertTrue(self.g_algo.save_to_json("../data/testCase1.txt"))
        self.assertTrue(self.g_algo.load_from_json("../data/testCase1.txt"))
        self.assertTrue(self.g_algo.load_from_json("../data/A0"))
