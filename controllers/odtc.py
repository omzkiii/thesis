
import networkx as nx
import numpy as np
import math
import itertools
import time
from decimal import Decimal



def odtc(graph, origin_nodes, dest_nodes):
    """
    Selects the central node in the graph using Origin Destination TC

    Parameters
    ----------------------------------
    graph: networkx graph
    origin_nodes: list of origin nodes in graph
    dest_nodes: list of destination nodes in graph

    
    Returns
    ----------------------------------
    central_node: node id of central node
    """
    size = graph.number_of_nodes()
    v_ratios = np.zeros((size, 1), dtype=Decimal)
    beta_value = 0.1
    leaf_nodes = get_leafnodes(graph)
    

    # for analyzing runtime
    start = time.time()

    for origin in origin_nodes:
        for dest in dest_nodes:
            all_paths = list(nx.all_simple_paths(graph, origin, dest))
            
            if(len(all_paths) > 0):
                all_path_nodes = set(itertools.chain(*list(all_paths)))
                non_leaf_nodes  = set(all_path_nodes) - set(leaf_nodes)
                final_v = set(non_leaf_nodes) - set([origin, dest])
                for v in final_v:
                    v_paths = [path for path in all_paths if v in path]
                    
                    if (len(v_paths)> 0):
                        if(int(len(v_paths)) == int(len(all_paths))):
                            ratio = 1
                        else:

                            all_paths_costs = path_cost(all_paths, beta_value)
                            v_costs = path_cost(v_paths, beta_value)
                            ratio = v_costs / all_paths_costs
                        v_ratios[v] += ratio
                           
    print('\t*END of usingNX fxn w/execution time:', time.time() - start, '\n\n' )
    
    central_node = v_ratios.max()

    return central_node



def get_leafnodes(G):
    leaf_dictionary = dict.fromkeys(G.nodes(),0)
    leaf_nodes = []
    is_directed_flag = nx.is_directed(G)
    for node in G.nodes():
        if is_directed_flag:        
            if(G.in_degree(node) == 0 or G.out_degree(node) == 0):
                leaf_nodes.append(node)
        else:
            if(len(G[node]) < 2):
                leaf_nodes.append(node)
    return leaf_nodes




def path_cost(paths, beta_value):
    cost_all = [len(path)-1 for path in paths]
    e_cost_all = [math.exp(-1*beta_value*cost) for cost in cost_all]
    paths_costs = sum(e_cost_all)
    return Decimal(paths_costs)

    


if __name__ == "__main__":
    pass
    # odtc()
