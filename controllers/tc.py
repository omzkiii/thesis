import networkx as nx
import numpy as np
import math
import itertools
import time
from decimal import Decimal


def get_central_node(graph):
    """
    Selects the central node in the graph using unmodified TC

    Parameters
    ----------------------------------
    graph: networkx graph


    Returns
    ----------------------------------
    central_node: node id of central node
    """
    all_nodes = list(graph.nodes())
    size = graph.number_of_nodes()
    v_ratios = dict.fromkeys(graph.nodes(), 0)
    beta_value = 0.1
    leaf_nodes = get_leafnodes(graph)

    # for analyzing runtime
    start = time.time()

    for src in all_nodes:
        targets = set(all_nodes) - set([src])
        for target in targets:
            all_paths = list(nx.all_simple_paths(graph, src, target))

            if len(all_paths) > 0:
                all_path_nodes = set(itertools.chain(*list(all_paths)))
                non_leaf_nodes = set(all_path_nodes) - set(leaf_nodes)
                final_v = set(non_leaf_nodes) - set([src, target])
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

    print("\t*END of usingNX fxn w/execution time:", time.time() - start, "\n\n")

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


def tc(subgraphs):
    total_tc_nodes = 0
    start_time = time.time()
    central_nodes = set()
    for key, values in subgraphs.items():
        central_node = get_central_node(values[0])
        print("=====================")
        print(key)
        print("central: ", central_node)
        print("=====================\n\n")
        central_nodes.add(central_node)
        total_tc_nodes += values[0].number_of_nodes()
    total_time = time.time() - start_time
    print(central_nodes)
    return central_nodes, total_time, len(central_nodes), total_tc_nodes


if __name__ == "__main__":
    pass
    # tc()
