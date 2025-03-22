from get_graph import get_graph
from gui import gui
from construct_graph import construct_graph
from runtime import runtime
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc


def generate(place_name, amenities):
    filename = f"{place_name} - {amenities[0]}"
    graph, nodes, edges, landmarks = get_graph(place_name, amenities=amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    terminal_nodes = odtc(subgraphs)
    # terminal_nodes = random.sample(list(graph.nodes), 10)
    route = steiner_network(graph, nodes, edges, terminal_nodes[0])
    construct_graph(nodes, edges, subgraphs, landmarks, terminal_nodes, route, filename)


def evaluation(location, distance, amenities):
    graph, nodes, edges, landmarks = get_graph(location, distance, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    (
        odtc_nodes,
        odtc_time,
        odtc_central_nodes_count,
        total_origin_nodes,
        total_dest_nodes,
        total_odtc_nodes,
    ) = odtc(subgraphs)
    tc_nodes, tc_time, tc_central_nodes_count, total_tc_nodes = tc(subgraphs)
    runtime(
        graph_type,
        location,
        odtc_time,
        odtc_central_nodes_count,
        total_origin_nodes,
        total_dest_nodes,
        total_odtc_nodes,
        tc_time,
        tc_central_nodes_count,
        total_tc_nodes,
    )


"""
def evaluation(center_point, distance, amenities):
    graph, nodes, edges, landmarks = get_graph(center_point, distance, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    odtc_nodes, odtc_time, odtc_nodes_count = odtc(subgraphs)
    tc_nodes, tc_time, tc_nodes_count = tc(subgraphs)
    # tc()
    # steiner_network()
    runtime(graph_type, place_name, odtc_time, tc_time, odtc_nodes_count, tc_nodes_count)
"""

if __name__ == "__main__":
    """
    Instruction:
    First input the type of graph

    then if you have place_name use the "evaluation("Sampaloc, Manila", None, ["school", "college", "institute", "university"])

    otherwise use the coordinates below of it
    """

    
    graph_type = "Ring"
    #evaluation("Quiapo, Manila", None, ["school", "college", "institute", "university"])
    coordinates = ((14.6514, 121.0497))  # Latitude, Longitude
    distance_meters = 2000  
    #evaluation(
    #    coordinates,
    #    distance_meters,
    #    ["school", "college", "institute", "university"]
    #)


    total_runs = 500
    successful_runs = 0

    for run_num in range(1, total_runs + 1):
        print(f"\n=== Run {run_num}/{total_runs} ===")
        try:
            #evaluation("Quiapo, Manila", None, ["school", "college", "institute", "university"])
            evaluation(
               coordinates,
                distance_meters,
                ["school", "college", "institute", "university"],
            )
            successful_runs += 1
        except KeyboardInterrupt:
            print("\nUser interrupted the process")
            break
        except Exception as e:
            print(f"Critical error: {str(e)}")
            break

    print(f"\nCompleted {successful_runs}/{total_runs} successful runs")
    if successful_runs > 0:
       print("Check execution_times.csv for results")