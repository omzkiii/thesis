import osmnx as ox
import networkx as nx
from itertools import product
from itertools import permutations
import random


def steiner_network(graph, nodes, edges, terminal_nodes):
    terminals = list(terminal_nodes)
    d = float("inf")
    B = None
    for u, v in product(graph.nodes, repeat=2):
        s = {}
        node_u = u
        node_v = v
        for a, b in permutations(terminals, 2):
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

        s = dict(sorted(s.items(), key=lambda item: item[1]))
        print(s)
        C = nx.shortest_path_length(graph, node_u, node_v)
        p = len(s)
        for key, value in s.items():
            C = C + value
            if (float(C) / float(p)) <= float(d) and value != 0:
                d = float(C) / float(p)
                B = (u, v), s, key

    print("====================================================")
    print("====================================================")
    print("====================================================")
    print(B)


if __name__ == "__main__":
    print("Starting Steiner Network")
