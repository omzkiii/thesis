import osmnx as ox
import networkx as nx
from itertools import product
import random


def steiner_network(graph, nodes, edges, terminal_nodes):
    random_nodes = random.sample(list(graph.nodes), 10)
    d = float("inf")
    B = None
    for u, v in product(graph.nodes, repeat=2):
        s = {}
        node_u = u
        node_v = v
        for a, b in product(random_nodes, repeat=2):
            node_a = a
            node_b = b
            shortest_path_a = nx.shortest_path_length(
                graph, node_a, node_u, weight=None, method="dijkstra"
            )
            shortest_path_b = nx.shortest_path_length(
                graph, node_b, node_v, weight=None, method="dijkstra"
            )
            # s[shortest_path_a + shortest_path_b] = (node_a, node_b)
            shortest_path = shortest_path_a + shortest_path_b
            s[(node_a, node_b)] = shortest_path

        s = dict(sorted(s.items()))
        print(s)
        p = len(s)
        C = nx.shortest_path_length(graph, node_u, node_v)
        for key in s:
            # print(C)
            C = C + key[1]
            # print(s, C)
            if C / p <= d:
                d = C / p
                B = (u, v), s, key

    print("====================================")
    print("====================================")
    print("====================================")
    print("====================================")
    print(B)


if __name__ == "__main__":
    print("Starting Steiner Network")
