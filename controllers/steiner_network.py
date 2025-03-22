import json
import osmnx as ox
import networkx as nx
from itertools import product
from itertools import permutations
import random


def steiner_network(graph, nodes, edges, terminal_nodes):
    terminals = list(terminal_nodes)
    d = float("inf")
    B = {}
    for u, v in product(graph.nodes, repeat=2):
        sc = {}
        node_u = u
        node_v = v
        for a, b in permutations(terminals, 2):
            node_a = a
            node_b = b
            shortest_cost_a = nx.shortest_path_length(
                graph, node_a, node_u, weight=None, method="dijkstra"
            )
            shortest_cost_b = nx.shortest_path_length(
                graph, node_v, node_b, weight=None, method="dijkstra"
            )
            shortest_path_cost = shortest_cost_a + shortest_cost_b
            sc[(node_a, node_b)] = shortest_path_cost

        sc = dict(sorted(sc.items(), key=lambda item: item[1]))
        C = nx.shortest_path_length(graph, node_u, node_v)
        p = len(sc)
        # i = 1
        pairs = []
        for key, value in sc.items():
            C = C + value
            pairs.append(key)
            if (float(C) / float(p)) < float(d):
                B = {}
                d = float(C) / float(p)
                B[node_u, node_v] = pairs
    shortest_paths = set()
    for key, values in B.items():
        for pair in values:
            shortest_path_a = nx.shortest_path(
                graph, pair[0], key[0], weight=None, method="dijkstra"
            )
            shortest_path_b = nx.shortest_path(
                graph, key[1], pair[1], weight=None, method="dijkstra"
            )
            shortest_paths.update(zip(shortest_path_a, shortest_path_a[1:]))
            shortest_paths.update(zip(shortest_path_b, shortest_path_b[1:]))

    route = edges[edges.index.isin(list(shortest_paths))]
    total_distance = route["length"].sum()
    print("=================")
    print(total_distance)
    print("=================")
    with open("routes_modified.json", "w") as file:
        json.dump(list(shortest_paths), file, indent=4)
    path_check(edges, list(shortest_paths))
    return route


def preload_steiner_network(edges):
    shortest_paths = []
    with open("routes_modified.json", "r") as file:
        shortest_paths = json.load(file)  # Converts JSON back to a Python list
    route = edges[edges.index.isin(list(shortest_paths))]
    return route


def path_check(edges, route):
    edges_path = []
    for edge_tuple, edge in edges.iterrows():
        x, y, _ = edge_tuple
        edges_path.append((x, y))
    two_way = 0
    one_way = 0
    for i in range(len(route)):
        x, y = route[i]
        if (y, x) in edges_path:
            two_way += 1
        else:
            one_way += 1
        print(f"Two Way: {two_way} \nOne Way: {one_way}")


if __name__ == "__main__":
    print("Starting Steiner Network")
