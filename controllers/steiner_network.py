import osmnx as ox
import networkx as nx
from itertools import product
import random


def steiner_network(graph, nodes, edges, terminal_nodes):
    if nx.is_strongly_connected(graph):
        print("The graph is closed (connected).")
    else:
        print("The graph is not closed (not connected).")
    # random_nodes = random.sample(list(graph.nodes), 10)
    # print(len(nodes))
    # for u, v in product(graph.nodes, repeat=2):
    #     s = {}
    #     node_u = u
    #     node_v = v
    #     for a, b in product(random_nodes, repeat=2):
    #         node_a = a
    #         node_b = b
    #         shortest_path_a = nx.shortest_path_length(
    #             graph, node_a, node_u, weight=None, method="dijkstra"
    #         )
    #         shortest_path_b = nx.shortest_path_length(
    #             graph, node_b, node_v, weight=None, method="dijkstra"
    #         )
    #         s[shortest_path_a + shortest_path_b] = (node_a, node_b)
    #
    #     s = dict(sorted(s.items()))
    #     C = nx.shortest_path_length(graph, node_u, node_v)
    #     print(C)


if __name__ == "__main__":
    print("Starting Steiner Network")
