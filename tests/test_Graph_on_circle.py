from src.GraphAlgo import GraphAlgo


def create_g_10_80_1():
    graph = GraphAlgo()
    graph.load_from_json("../data/Graph_on_circle/G_10_80_1.json")
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_100_800_1():
    graph = GraphAlgo()
    graph.load_from_json("../data/Graph_on_circle/G_100_800_1.json")
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_1000_8000_1():
    graph = GraphAlgo()
    graph.load_from_json("../data/Graph_on_circle/G_1000_8000_1.json")
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_10000_80000_1():
    graph = GraphAlgo()
    graph.load_from_json("../data/Graph_on_circle/G_10000_80000_1.json")
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_20000_160000_1():
    graph = GraphAlgo()
    graph.load_from_json("../data/Graph_on_circle/G_20000_160000_1.json")
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_30000_240000_1():
    graph = GraphAlgo()
    graph.load_from_json("../data/Graph_on_circle/G_30000_240000_1.json")
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


if __name__ == '__main__':
    create_g_10_80_1()
    create_g_100_800_1()
    create_g_1000_8000_1()
    create_g_10000_80000_1()
    create_g_20000_160000_1()
    create_g_30000_240000_1()
