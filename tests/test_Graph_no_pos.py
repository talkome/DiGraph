import json
import time

import networkx as nx

from src.GraphAlgo import GraphAlgo


def create_g_10_80_0():
    graph = GraphAlgo()
    g_nx = nx.DiGraph()
    file = "../data/Graph_no_pos/G_10_80_0.json"
    graph.load_from_json(file)
    try:
        with open(file, 'r') as file:
            load_file = json.load(file)

        for vertex in load_file["Nodes"]:
            g_nx.add_node(vertex["id"])

        for edge in load_file["Edges"]:
            g_nx.add_weighted_edges_from([(edge["src"], edge["dest"], edge["w"])])
    except Exception as ex:
        print("couldn't save to jason", ex)
        return False
    finally:
        file.close()

    # graph.plot_graph()

    print("g_10_80_0 result:")
    shortest_path_result = []
    start_time = time.perf_counter()
    dist, path = graph.shortest_path(2, 8)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(2, 8)=", path)
    print("distance=", dist)

    shortest_path_networkx_result = []
    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=2, target=8)
    dist = nx.shortest_path_length(G=g_nx, source=2, target=8)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10_80_0 networkx result:")
    print("shortest_path(2,8)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(3, 9)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(3, 9)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=3, target=9)
    dist = nx.shortest_path_length(G=g_nx, source=3, target=9)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10_80_0 networkx result:")
    print("shortest_path(3,9)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(4, 7)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(4, 7)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=4, target=7)
    dist = nx.shortest_path_length(G=g_nx, source=4, target=7)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10_80_0 networkx result:")
    print("shortest_path(4,7)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 4)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 4)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=4)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10_80_0 networkx result:")
    print("shortest_path(5,4)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 2)=", path)
    print("distance=", dist)
    result = sum(shortest_path_result) / len(shortest_path_result)
    print("shortest path record:", result)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=2)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_networkx_result.append(record)
    print("g_10_80_0 networkx result:")
    print("shortest_path(5,2)", path)
    print("distance=", dist)
    result = sum(shortest_path_networkx_result) / len(shortest_path_networkx_result)
    print("networkx shortest path record:", result)

    start_time = time.perf_counter()
    path = graph.connected_components()
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_components=", path)
    print("connected components record:", record)

    start_time = time.perf_counter()
    cc = nx.strongly_connected_components(G=g_nx)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10_80_0 networkx result:")
    print("strongly_connected_components(G=g)", cc)
    print("networkx connected components record:", record)

    connected_component_result = []
    start_time = time.perf_counter()
    cc = graph.connected_component(1)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(1)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(2)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(2)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(3)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(3)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(4)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(5)
    end_time = time.perf_counter()
    record = end_time - start_time
    connected_component_result.append(record)
    print("connected_component(5)", cc)
    result = sum(connected_component_result) / len(connected_component_result)
    print("connected component record:", result)


def create_g_100_800_0():
    graph = GraphAlgo()
    g_nx = nx.DiGraph()
    file = "../data/Graph_no_pos/G_100_800_0.json"
    graph.load_from_json(file)
    try:
        with open(file, 'r') as file:
            load_file = json.load(file)

        for vertex in load_file["Nodes"]:
            g_nx.add_node(vertex["id"])

        for edge in load_file["Edges"]:
            g_nx.add_weighted_edges_from([(edge["src"], edge["dest"], edge["w"])])
    except Exception as ex:
        print("couldn't save to jason", ex)
        return False
    finally:
        file.close()

    # graph.plot_graph()

    print("g_100_800_0 result:")
    shortest_path_result = []
    start_time = time.perf_counter()
    dist, path = graph.shortest_path(2, 8)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(2, 8)=", path)
    print("distance=", dist)

    shortest_path_networkx_result = []
    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=2, target=8)
    dist = nx.shortest_path_length(G=g_nx, source=2, target=8)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_100_800_0 networkx result:")
    print("shortest_path(2,8)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(3, 9)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(3, 9)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=3, target=9)
    dist = nx.shortest_path_length(G=g_nx, source=3, target=9)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_100_800_0 networkx result:")
    print("shortest_path(3,9)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(4, 7)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(4, 7)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=4, target=7)
    dist = nx.shortest_path_length(G=g_nx, source=4, target=7)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_100_800_0 networkx result:")
    print("shortest_path(4,7)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 4)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 4)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=4)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_100_800_0 networkx result:")
    print("shortest_path(5,4)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 2)=", path)
    print("distance=", dist)
    result = sum(shortest_path_result) / len(shortest_path_result)
    print("shortest path record:", result)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=2)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_networkx_result.append(record)
    print("g_100_800_0 networkx result:")
    print("shortest_path(5,2)", path)
    print("distance=", dist)
    result = sum(shortest_path_networkx_result) / len(shortest_path_networkx_result)
    print("networkx shortest path record:", result)

    start_time = time.perf_counter()
    path = graph.connected_components()
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_components=", path)
    print("connected components record:", record)

    start_time = time.perf_counter()
    cc = nx.strongly_connected_components(G=g_nx)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_100_800_0 networkx result:")
    print("strongly_connected_components(G=g)", cc)
    print("networkx connected components record:", record)

    connected_component_result = []
    start_time = time.perf_counter()
    cc = graph.connected_component(1)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(1)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(2)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(2)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(3)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(3)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(4)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(5)
    end_time = time.perf_counter()
    record = end_time - start_time
    connected_component_result.append(record)
    print("connected_component(5)", cc)
    result = sum(connected_component_result) / len(connected_component_result)
    print("connected component record:", result)


def create_g_1000_8000_0():
    graph = GraphAlgo()
    g_nx = nx.DiGraph()
    file = "../data/Graph_no_pos/G_1000_8000_0.json"
    graph.load_from_json(file)
    try:
        with open(file, 'r') as file:
            load_file = json.load(file)

        for vertex in load_file["Nodes"]:
            g_nx.add_node(vertex["id"])

        for edge in load_file["Edges"]:
            g_nx.add_weighted_edges_from([(edge["src"], edge["dest"], edge["w"])])
    except Exception as ex:
        print("couldn't save to jason", ex)
        return False
    finally:
        file.close()

    # graph.plot_graph()

    print("g_1000_8000_0 result:")
    shortest_path_result = []
    start_time = time.perf_counter()
    dist, path = graph.shortest_path(2, 8)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(2, 8)=", path)
    print("distance=", dist)

    shortest_path_networkx_result = []
    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=2, target=8)
    dist = nx.shortest_path_length(G=g_nx, source=2, target=8)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_1000_8000_0 networkx result:")
    print("shortest_path(2,8)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(3, 9)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(3, 9)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=3, target=9)
    dist = nx.shortest_path_length(G=g_nx, source=3, target=9)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_1000_8000_0 networkx result:")
    print("shortest_path(3,9)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(4, 7)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(4, 7)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=4, target=7)
    dist = nx.shortest_path_length(G=g_nx, source=4, target=7)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_1000_8000_0 networkx result:")
    print("shortest_path(4,7)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 4)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 4)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=4)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_1000_8000_0 networkx result:")
    print("shortest_path(5,4)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 2)=", path)
    print("distance=", dist)
    result = sum(shortest_path_result) / len(shortest_path_result)
    print("shortest path record:", result)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=2)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_networkx_result.append(record)
    print("g_1000_8000_0 networkx result:")
    print("shortest_path(5,2)", path)
    print("distance=", dist)
    result = sum(shortest_path_networkx_result) / len(shortest_path_networkx_result)
    print("networkx shortest path record:", result)

    start_time = time.perf_counter()
    path = graph.connected_components()
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_components=", path)
    print("connected components record:", record)

    start_time = time.perf_counter()
    cc = nx.strongly_connected_components(G=g_nx)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_1000_8000_0 networkx result:")
    print("strongly_connected_components(G=g)", cc)
    print("networkx connected components record:", record)

    connected_component_result = []
    start_time = time.perf_counter()
    cc = graph.connected_component(1)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(1)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(2)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(2)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(3)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(3)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(4)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(5)
    end_time = time.perf_counter()
    record = end_time - start_time
    connected_component_result.append(record)
    print("connected_component(5)", cc)
    result = sum(connected_component_result) / len(connected_component_result)
    print("connected component record:", result)


def create_g_10000_80000_0():
    graph = GraphAlgo()
    g_nx = nx.DiGraph()
    file = "../data/Graph_no_pos/G_10000_80000_0.json"
    graph.load_from_json(file)
    try:
        with open(file, 'r') as file:
            load_file = json.load(file)

        for vertex in load_file["Nodes"]:
            g_nx.add_node(vertex["id"])

        for edge in load_file["Edges"]:
            g_nx.add_weighted_edges_from([(edge["src"], edge["dest"], edge["w"])])
    except Exception as ex:
        print("couldn't save to jason", ex)
        return False
    finally:
        file.close()

    # graph.plot_graph()

    print("g_10000_80000_0 result:")
    shortest_path_result = []
    start_time = time.perf_counter()
    dist, path = graph.shortest_path(2, 8)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(2, 8)=", path)
    print("distance=", dist)

    shortest_path_networkx_result = []
    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=2, target=8)
    dist = nx.shortest_path_length(G=g_nx, source=2, target=8)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10000_80000_0 networkx result:")
    print("shortest_path(2,8)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(3, 9)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(3, 9)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=3, target=9)
    dist = nx.shortest_path_length(G=g_nx, source=3, target=9)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10000_80000_0 networkx result:")
    print("shortest_path(3,9)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(4, 7)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(4, 7)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=4, target=7)
    dist = nx.shortest_path_length(G=g_nx, source=4, target=7)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10000_80000_0 networkx result:")
    print("shortest_path(4,7)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 4)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 4)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=4)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10000_80000_0 networkx result:")
    print("shortest_path(5,4)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 2)=", path)
    print("distance=", dist)
    result = sum(shortest_path_result) / len(shortest_path_result)
    print("shortest path record:", result)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=2)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_networkx_result.append(record)
    print("g_10000_80000_0 networkx result:")
    print("shortest_path(5,2)", path)
    print("distance=", dist)
    result = sum(shortest_path_networkx_result) / len(shortest_path_networkx_result)
    print("networkx shortest path record:", result)

    start_time = time.perf_counter()
    path = graph.connected_components()
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_components=", path)
    print("connected components record:", record)

    start_time = time.perf_counter()
    cc = nx.strongly_connected_components(G=g_nx)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_10000_80000_0 networkx result:")
    print("strongly_connected_components(G=g)", cc)
    print("networkx connected components record:", record)

    connected_component_result = []
    start_time = time.perf_counter()
    cc = graph.connected_component(1)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(1)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(2)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(2)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(3)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(3)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(4)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(5)
    end_time = time.perf_counter()
    record = end_time - start_time
    connected_component_result.append(record)
    print("connected_component(5)", cc)
    result = sum(connected_component_result) / len(connected_component_result)
    print("connected component record:", result)


def create_g_20000_160000_0():
    graph = GraphAlgo()
    g_nx = nx.DiGraph()
    file = "../data/Graph_no_pos/G_20000_160000_0.json"
    graph.load_from_json(file)
    try:
        with open(file, 'r') as file:
            load_file = json.load(file)

        for vertex in load_file["Nodes"]:
            g_nx.add_node(vertex["id"])

        for edge in load_file["Edges"]:
            g_nx.add_weighted_edges_from([(edge["src"], edge["dest"], edge["w"])])
    except Exception as ex:
        print("couldn't save to jason", ex)
        return False
    finally:
        file.close()

    # graph.plot_graph()

    print("g_20000_160000_0 result:")
    shortest_path_result = []
    start_time = time.perf_counter()
    dist, path = graph.shortest_path(2, 8)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(2, 8)=", path)
    print("distance=", dist)

    shortest_path_networkx_result = []
    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=2, target=8)
    dist = nx.shortest_path_length(G=g_nx, source=2, target=8)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_20000_160000_0 networkx result:")
    print("shortest_path(2,8)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(3, 9)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(3, 9)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=3, target=9)
    dist = nx.shortest_path_length(G=g_nx, source=3, target=9)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_20000_160000_0 networkx result:")
    print("shortest_path(3,9)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(4, 7)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(4, 7)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=4, target=7)
    dist = nx.shortest_path_length(G=g_nx, source=4, target=7)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_20000_160000_0 networkx result:")
    print("shortest_path(4,7)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 4)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 4)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=4)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_20000_160000_0 networkx result:")
    print("shortest_path(5,4)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 2)=", path)
    print("distance=", dist)
    result = sum(shortest_path_result) / len(shortest_path_result)
    print("shortest path record:", result)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=2)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_networkx_result.append(record)
    print("g_20000_160000_0 networkx result:")
    print("shortest_path(5,2)", path)
    print("distance=", dist)
    result = sum(shortest_path_networkx_result) / len(shortest_path_networkx_result)
    print("networkx shortest path record:", result)

    start_time = time.perf_counter()
    path = graph.connected_components()
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_components=", path)
    print("connected components record:", record)

    start_time = time.perf_counter()
    cc = nx.strongly_connected_components(G=g_nx)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_20000_160000_0 networkx result:")
    print("strongly_connected_components(G=g)", cc)
    print("networkx connected components record:", record)

    connected_component_result = []
    start_time = time.perf_counter()
    cc = graph.connected_component(1)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(1)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(2)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(2)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(3)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(3)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(4)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(5)
    end_time = time.perf_counter()
    record = end_time - start_time
    connected_component_result.append(record)
    print("connected_component(5)", cc)
    result = sum(connected_component_result) / len(connected_component_result)
    print("connected component record:", result)


def create_g_30000_240000_0():
    graph = GraphAlgo()
    g_nx = nx.DiGraph()
    file = "../data/Graph_no_pos/G_30000_240000_0.json"
    graph.load_from_json(file)
    try:
        with open(file, 'r') as file:
            load_file = json.load(file)

        for vertex in load_file["Nodes"]:
            g_nx.add_node(vertex["id"])

        for edge in load_file["Edges"]:
            g_nx.add_weighted_edges_from([(edge["src"], edge["dest"], edge["w"])])
    except Exception as ex:
        print("couldn't save to jason", ex)
        return False
    finally:
        file.close()

    # graph.plot_graph()

    print("g_30000_240000_0 result:")
    shortest_path_result = []
    start_time = time.perf_counter()
    dist, path = graph.shortest_path(2, 8)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(2, 8)=", path)
    print("distance=", dist)

    shortest_path_networkx_result = []
    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=2, target=8)
    dist = nx.shortest_path_length(G=g_nx, source=2, target=8)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_30000_240000_0 networkx result:")
    print("shortest_path(2,8)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(3, 9)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(3, 9)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=3, target=9)
    dist = nx.shortest_path_length(G=g_nx, source=3, target=9)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_30000_240000_0 networkx result:")
    print("shortest_path(3,9)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(4, 7)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(4, 7)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=4, target=7)
    dist = nx.shortest_path_length(G=g_nx, source=4, target=7)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_30000_240000_0 networkx result:")
    print("shortest_path(4,7)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 4)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 4)=", path)
    print("distance=", dist)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=4)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_30000_240000_0 networkx result:")
    print("shortest_path(5,4)", path)
    print("distance=", dist)
    shortest_path_networkx_result.append(record)

    start_time = time.perf_counter()
    dist, path = graph.shortest_path(5, 2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_result.append(record)
    print("shortest_path(5, 2)=", path)
    print("distance=", dist)
    result = sum(shortest_path_result) / len(shortest_path_result)
    print("shortest path record:", result)

    start_time = time.perf_counter()
    path = nx.shortest_path(G=g_nx, source=5, target=2)
    dist = nx.shortest_path_length(G=g_nx, source=5, target=2)
    end_time = time.perf_counter()
    record = end_time - start_time
    shortest_path_networkx_result.append(record)
    print("g_30000_240000_0 networkx result:")
    print("shortest_path(5,2)", path)
    print("distance=", dist)
    result = sum(shortest_path_networkx_result) / len(shortest_path_networkx_result)
    print("networkx shortest path record:", result)

    start_time = time.perf_counter()
    path = graph.connected_components()
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_components=", path)
    print("connected components record:", record)

    start_time = time.perf_counter()
    cc = nx.strongly_connected_components(G=g_nx)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("g_30000_240000_0 networkx result:")
    print("strongly_connected_components(G=g)", cc)
    print("networkx connected components record:", record)

    connected_component_result = []
    start_time = time.perf_counter()
    cc = graph.connected_component(1)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(1)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(2)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(2)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(3)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(3)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(4)
    end_time = time.perf_counter()
    record = end_time - start_time
    print("connected_component(4)", cc)
    connected_component_result.append(record)

    start_time = time.perf_counter()
    cc = graph.connected_component(5)
    end_time = time.perf_counter()
    record = end_time - start_time
    connected_component_result.append(record)
    print("connected_component(5)", cc)
    result = sum(connected_component_result) / len(connected_component_result)
    print("connected component record:", result)


if __name__ == '__main__':
    create_g_10_80_0()
    create_g_100_800_0()
    create_g_1000_8000_0()
    # create_g_10000_80000_0()
    # create_g_20000_160000_0()
    # create_g_30000_240000_0()
