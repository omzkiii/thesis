import osmnx as ox
import networkx as nx
from itertools import product
from itertools import permutations
import random


def steiner_network(graph, nodes, edges, terminal_nodes):
    terminals = list(terminal_nodes)
    # terminals = random.sample(list(graph.nodes), 5)
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
                graph, node_b, node_v, weight=None, method="dijkstra"
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
            print("=================")
            print("=================")
            print(B)
            print("=================")
            print("=================")
    shortest_paths = set()
    for key, values in B.items():
        for pair in values:
            shortest_path_a = nx.shortest_path(
                graph, pair[0], key[0], weight=None, method="dijkstra"
            )
            shortest_path_b = nx.shortest_path(
                graph, pair[1], key[1], weight=None, method="dijkstra"
            )
            shortest_paths.update(zip(shortest_path_a, shortest_path_a[1:]))
            shortest_paths.update(zip(shortest_path_b, shortest_path_b[1:]))

    route = edges[edges.index.isin(list(shortest_paths))]
    total_distance = route["length"].sum()
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print(total_distance)
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    print("=================")
    return route


if __name__ == "__main__":
    print("Starting Steiner Network")
