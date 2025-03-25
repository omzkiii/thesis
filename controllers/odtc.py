import networkx as nx
import math
import itertools
import time
from decimal import Decimal


def get_central_node(graph, origin_nodes, dest_nodes):
    """
    Selects the central node in the graph using Origin Destination TC

    Parameters
    ----------------------------------
    graph: networkx graph
    origin_nodes: list of origin nodes in graph
    dest_nodes: list of destination nodes in graph


    Returns
    ----------------------------------
    central_node: list with node id of central node/s
    """
    size = graph.number_of_nodes()
    v_ratios = dict.fromkeys(graph.nodes(), 0)
    beta_value = 0.1
    leaf_nodes = get_leafnodes(graph)

    # for analyzing runtime
    start = time.time()

    for origin in origin_nodes:
        for dest in dest_nodes:
            all_paths = list(nx.all_simple_paths(graph, origin, dest))

            if len(all_paths) > 0:
                all_path_nodes = set(itertools.chain(*list(all_paths)))
                non_leaf_nodes = set(all_path_nodes) - set(leaf_nodes)
                final_v = set(non_leaf_nodes) - set([origin, dest])
                for v in final_v:
                    v_paths = [path for path in all_paths if v in path]

                    if len(v_paths) > 0:
                        if int(len(v_paths)) == int(len(all_paths)):
                            ratio = 1
                        else:
                            all_paths_costs = path_cost(all_paths, beta_value)
                            v_costs = path_cost(v_paths, beta_value)
                            ratio = v_costs / all_paths_costs
                        v_ratios[v] += ratio

    # print("\t*END of usingNX fxn w/execution time:", time.time() - start, "\n\n")

    max_centrality = max(v_ratios.values())

    central_node = [k for k, v in v_ratios.items() if v == max_centrality]
    central_node = central_node[0]

    return central_node


def get_leafnodes(G):
    leaf_nodes = []
    is_directed_flag = nx.is_directed(G)
    for node in G.nodes():
        if is_directed_flag:
            if G.in_degree(node) == 0 or G.out_degree(node) == 0:
                leaf_nodes.append(node)
        else:
            if len(G[node]) < 2:
                leaf_nodes.append(node)
    return leaf_nodes


def path_cost(paths, beta_value):
    cost_all = [len(path) - 1 for path in paths]
    e_cost_all = [math.exp(-1 * beta_value * cost) for cost in cost_all]
    paths_costs = sum(e_cost_all)
    return Decimal(paths_costs)


# def odtc(subgraphs, graph):
#    for values in subgraphs.values():
#       central_node = get_central_node(values[0], values[1], values[2])
#       print(central_node)
# def odtc_benchmark(subgraphs, graph):
#     total_time = 0
#     for values in subgraphs.values():
#         start = time.time()
#         central_node = get_central_node(values[0], values[1], values[2])
#         elapsed = time.time() - start
#         total_time += elapsed
#         print(central_node)
#     return total_time


def odtc(subgraphs):
    central_nodes = set()
    origin_nodes = set()
    dest_nodes = set()
    total_odtc_nodes = 0
    start_time = time.time()
    for key, values in subgraphs.items():
        central_node = get_central_node(values[0], values[1], values[2])
        print("=====================")
        print(key)
        print("origin: ", values[1])
        print("dest: ", values[2])
        print("central: ", central_node)
        print("=====================\n\n")
        central_nodes.add(central_node)
        origin_nodes.update(values[1])
        dest_nodes.update(values[2])
        total_odtc_nodes += values[0].number_of_nodes()
    total_time = time.time() - start_time
    print(central_nodes)
    total_origin_nodes = len(origin_nodes)
    total_dest_nodes = len(dest_nodes)
    return (
        central_nodes,
        total_time,
        len(central_nodes),
        total_origin_nodes,
        total_dest_nodes,
        total_odtc_nodes,
    )


if __name__ == "__main__":
    pass
