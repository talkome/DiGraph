from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def check0():
    my_graph = DiGraph()
    for i in range(6):
        my_graph.add_node(i)

    my_graph.add_edge(0, 1, 3)
    my_graph.add_edge(1, 2, 1)
    my_graph.add_edge(2, 0, 20)
    my_graph.add_edge(1, 3, 5)
    my_graph.add_edge(1, 4, 7)

    my_graph.remove_edge(2, 0)
    num_of_edges = 4
    num_of_nodes = 5
    print(num_of_edges, my_graph.e_size)
    print(num_of_nodes, my_graph.v_size)

    my_graph.remove_edge(1, 2)
    num_of_edges = 3
    print(num_of_edges, my_graph.e_size)
    my_graph.remove_node(2)
    num_of_nodes = 4
    print(num_of_nodes, my_graph.v_size)
    print("graph:", my_graph.graph_vertices.keys())

    print("sons:", my_graph.sons.keys())
    print("fathers:", my_graph.fathers.keys())
    my_graph.add_edge(0, 3, 4)
    print("sons:", my_graph.sons.keys())
    print("fathers:", my_graph.fathers.keys())
    my_graph.remove_edge(0, 1)
    print("remove edge (0,1)")
    print("sons:", my_graph.sons.keys())
    print("fathers:", my_graph.fathers.keys())
    print(my_graph.graph_vertices.keys())


def check1():
    g1 = GraphAlgo()
    for node in range(5):
        g1.graph.add_node(node)

    g1.graph.add_edge(1, 0, 1)
    g1.graph.add_edge(0, 2, 4)
    g1.graph.add_edge(2, 1, 11)
    g1.graph.add_edge(0, 3, 7)
    g1.graph.add_edge(3, 4, 5)

    print(g1.connected_components())  # [[0, 1, 2], [3], [4]]
    print(g1.connected_component(0))  # [0, 1, 2]


def check2():
    g2 = GraphAlgo()
    for node in range(4):
        g2.graph.add_node(node)

    g2.graph.add_edge(0, 1, 1)
    g2.graph.add_edge(1, 0, 1.1)
    g2.graph.add_edge(1, 3, 1.8)
    g2.graph.add_edge(1, 2, 1.3)
    g2.graph.add_edge(2, 3, 1.1)

    print(g2.connected_components())  # [[2, 1, 0], [3]]
    print(g2.connected_component(0))  # [2, 1, 0]
    print(g2.connected_component(3))  # [3]


if __name__ == '__main__':
    # check0()
    # check1()
    check2()
