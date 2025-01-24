import osmnx as ox
import networkx as nx
from itertools import product


def steiner_network(graph, nodes, edges, terminal_nodes):
    random_nodes = nodes.sample(n=10)
    # for _, edge in edges.iterrows():
    #     print(edge)
    print(type(random_nodes))

    # for (_, node1), (_, node2) in zip(
    #     nodes.iterrows(), nodes.iloc[1:].iterrows()
    # ):
    #     for (_, node1), (_, node2) in zip(
    #         random_nodes.iterrows(), random_nodes.iloc[1:].iterrows()
    #     ):
    #         shortest_path = ox.shortest_path(graph, node1.name, node2.name, weight="length")
    #         print("-----------------------------")
    #         print(shortest_path)

    # for idx1, node1 in random_nodes.iterrows():
    #     for idx2, node2 in random_nodes.iterrows():
    #         if idx1 != idx2:
    #             print(node1.name, node2.name)

    # for (a, _), (b, _) in product(nodes.iterrows(), repeat=2):
    #     try:
    #         shortest_path = nx.shortest_path_length(graph, a, b, weight="length")
    #         print("-----------------------------")
    #     except Exception as e:
    #         print(e)
    #         shortest_path = 0
    #     print(shortest_path)
    print(len(nodes))
    # for (u, _), (v, _) in permutations(nodes.iterrows()):
    #     for (a, _), (b, _) in permutations(random_nodes.iterrows()):
    # print(len(nodes))
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
