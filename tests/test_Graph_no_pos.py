from src.GraphAlgo import GraphAlgo


def create_g_10_80_0():
    graph = GraphAlgo()
    file = "../data/Graph_no_pos/G_10_80_0.json"
    graph.load_from_json(file)
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_100_800_0():
    graph = GraphAlgo()
    file = "../data/Graph_no_pos/G_100_800_0.json"
    graph.load_from_json(file)
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_1000_8000_0():
    graph = GraphAlgo()
    file = "../data/Graph_no_pos/G_1000_8000_0.json"
    graph.load_from_json(file)
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_10000_80000_0():
    graph = GraphAlgo()
    file = "../data/Graph_no_pos/G_10000_80000_0.json"
    graph.load_from_json(file)
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_20000_160000_0():
    graph = GraphAlgo()
    file = "../data/Graph_no_pos/G_20000_160000_0.json"
    graph.load_from_json(file)
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


def create_g_30000_240000_0():
    graph = GraphAlgo()
    file = "../data/Graph_no_pos/G_30000_240000_0.json"
    graph.load_from_json(file)
    graph.plot_graph()
    graph.shortest_path(2, 8)
    graph.connected_components()
    graph.connected_component(4)


if __name__ == '__main__':
    create_g_10_80_0()
    create_g_100_800_0()
    create_g_1000_8000_0()
    create_g_10000_80000_0()
    create_g_20000_160000_0()
    create_g_30000_240000_0()
