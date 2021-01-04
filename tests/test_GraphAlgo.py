from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def setUp(self) -> None:
        self.g_algo = GraphAlgo()
        for i in range(9):
            self.g_algo.graph.add_node(i)

        self.g_algo.graph.add_edge(0, 1, 3)
        self.g_algo.graph.add_edge(0, 2, 9)
        self.g_algo.graph.add_edge(2, 0, 11)
        self.g_algo.graph.add_edge(1, 2, 7)
        self.g_algo.graph.add_edge(2, 1, 13)
        self.g_algo.graph.add_edge(1, 3, 5)
        self.g_algo.graph.add_edge(1, 4, 22.2)
        self.g_algo.graph.add_edge(4, 1, 4)
        self.g_algo.graph.add_edge(3, 4, 12)
        self.g_algo.graph.add_edge(5, 4, 11)
        self.g_algo.graph.add_edge(6, 4, 7)
        self.g_algo.graph.add_edge(7, 3, 8)
        self.g_algo.graph.add_edge(8, 2, 10)

    def test_shortest_path(self):
        self.assertEqual(self.g_algo.shortest_path(1, 4), (17, [1, 3, 4]))
        ans = self.g_algo.shortest_path(0, 3)
        self.assertEqual(ans, (8, [0, 1, 3]))
        self.assertEqual(self.g_algo.shortest_path(0, 4), (20, [0, 1, 3, 4]))
        self.assertIsNone(self.g_algo.shortest_path(0, 7))

    def test_connected_component(self):
        print(self.g_algo.connected_components())
        self.assertEqual(self.g_algo.connected_components(), [[0, 1, 2, 8, 4, 3, 7, 5, 6]])
        g1 = GraphAlgo()
        for node in range(5):
            g1.graph.add_node(node)

        print(g1.graph.get_all_v().keys())
        g1.graph.add_edge(1, 0, 1)
        g1.graph.add_edge(0, 2, 4)
        g1.graph.add_edge(2, 1, 11)
        g1.graph.add_edge(0, 3, 7)
        g1.graph.add_edge(3, 4, 5)
        print(g1.graph.sons.keys())

        ans = g1.connected_components()
        self.assertEqual(ans, [[0, 1, 2], [3], [4]])

    def test_connected_components(self):
        ans = self.g_algo.connected_component(0)
        self.assertEqual(ans, [0, 1, 2])

        g2 = GraphAlgo()
        for node in range(5):
            g2.graph.add_node(node)

        print(g2.graph.get_all_v().keys())
        g2.graph.add_edge(1, 0, 1)
        g2.graph.add_edge(0, 2, 4)
        g2.graph.add_edge(2, 1, 11)
        g2.graph.add_edge(0, 3, 7)
        g2.graph.add_edge(3, 4, 5)
        print(g2.graph.sons.keys())

        self.assertEqual(g2.connected_component(0), [0, 1, 2])

    # def test_plot_graph(self):
    #     pass

    def test_save_load_from_json(self):
        self.assertTrue(self.g_algo.save_to_json("../data/testCase1.txt"))
        self.assertTrue(self.g_algo.load_from_json("../data/testCase1.txt"))
        self.assertTrue(self.g_algo.load_from_json("../data/A0"))
