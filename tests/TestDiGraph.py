# from unittest import TestCase
#
# from src.DiGraph import DiGraph
#
#
# def check():
#     check0()
#     check1()
#     check2()
#
#
# class TestDiGraph(TestCase):
#
#     def check0(self):
#         my_graph = DiGraph()
#         for i in range(6):
#             my_graph.add_node(i)
#         my_graph.add_edge(0, 1, 3)
#         my_graph.add_edge(1, 2, 1)
#         my_graph.add_edge(2, 0, 20)
#         my_graph.add_edge(1, 3, 5)
#         my_graph.add_edge(1, 4, 7)
#
#         # print("graph:", self.my_graph.graph_node.keys())
#         my_graph.remove_edge(2, 0)
#         num_of_edges = 4
#         num_of_nodes = 5
#         self.assertEqual(num_of_edges, my_graph.e_size)
#         self.assertEqual(num_of_nodes, my_graph.v_size)
#
#         my_graph.remove_edge(1, 2)
#         num_of_edges = 3
#         self.assertEqual(num_of_edges, my_graph.e_size)
#         my_graph.remove_node(2)
#         num_of_nodes = 4
#         self.assertEqual(num_of_nodes, my_graph.v_size)
#         print("graph:", my_graph.graph_node.keys())
#
#         print("sons:", my_graph.sons.keys())
#         print("fathers:", my_graph.fathers.keys())
#         my_graph.add_edge(0, 3, 4)
#         print("sons:", my_graph.sons.keys())
#         print("fathers:", my_graph.fathers.keys())
#         my_graph.remove_edge(0, 1)
#         print("remove edge (0,1)")
#         print("sons:", my_graph.sons.keys())
#         print("fathers:", my_graph.fathers.keys())
#         print(my_graph.graph_node.keys())
#
#
# if __name__ == '__main__':
#     check()
