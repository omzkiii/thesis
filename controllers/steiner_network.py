import osmnx as ox
import networkx as nx
from itertools import product


def steiner_network(graph, nodes, edges, terminal_nodes):
    random_nodes = nodes.sample(n=10)
    print(len(nodes))
    for (u, _), (v, _) in product(nodes.iterrows(), repeat=2):
        for (a, _), (b, _) in product(random_nodes.iterrows(), repeat=2):
            node_u = u
            node_v = v
            node_a = a
            node_b = b
            if nx.has_path(graph, node_a, node_u):
                shortest_path_a = nx.shortest_path_length(
                    graph, node_a, node_u, weight="length"
                )
                print(f"Shortest path between {node_a} and {node_u}: {shortest_path_a}")

            if nx.has_path(graph, node_b, node_v):
                shortest_path_b = nx.shortest_path_length(
                    graph, node_b, node_v, weight="length"
                )
                print(f"Shortest path between {node_b} and {node_v}: {shortest_path_b}")


if __name__ == "__main__":
    print("Starting Steiner Network")
