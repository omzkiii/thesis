from get_graph import get_graph
from construct_graph import construct_graph
from runtime import runtime
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc


def generate(place_name, amenities):
    graph, nodes, edges, landmarks = get_graph(place_name, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    terminal_nodes = odtc(subgraphs)
    steiner_network(graph, nodes, edges, terminal_nodes)
    # construct_graph(nodes, edges, subgraphs, landmarks)


def evaluation(center_point, distance, amenities):
    graph, nodes, edges, landmarks = get_graph(center_point, distance, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    odtc_nodes, odtc_time, odtc_nodes_count = odtc(subgraphs)
    tc_nodes, tc_time, tc_nodes_count = tc(subgraphs)
    # tc()
    # steiner_network()
    runtime(graph_type, place_name, odtc_time, tc_time, odtc_nodes_count, tc_nodes_count)


if __name__ == "__main__":
    #generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
    #evaluation("Sampaloc, Manila", ["school", "college", "institute", "university"])
        # Example usage for Sampaloc, Manila coordinates
    coordinates = (14.984113296438625, 120.90632193749528)  # Latitude, Longitude
    distance_meters = 2000  # 2km radius
    place_name = "Ulingao, Bulacan"
    graph_type = "Ring"
    
    #evaluation(
    #    coordinates,
    #    distance_meters,
    #    ["school", "college", "institute", "university"]
    #)

    total_runs = 500
    successful_runs = 0
    
    for run_num in range(1, total_runs+1):
        print(f"\n=== Run {run_num}/{total_runs} ===")
        try:
            evaluation(coordinates, distance_meters, ["school", "college", "institute", "university"])
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