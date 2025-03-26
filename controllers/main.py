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


if __name__ == "__main__":
    print("=== Transportation Centrality Evaluation ===")

    # Input: Graph type
    valid_graph_types = ["Grid", "Scale-Free", "Ring"]
    while True:
        graph_type = input("Enter graph type (Grid / Scale-Free / Ring): ").strip()
        if graph_type in valid_graph_types:
            break
        print("Invalid input. Please enter one of: Grid, Scale-Free, Ring")

    # Input: Location type
    while True:
        location_type = input("Do you want to input a place name or coordinates? (place/coord): ").strip().lower()
        if location_type in ["place", "coord"]:
            break
        print("Invalid input. Please enter either 'place' or 'coord'.")

    # Location input
    if location_type == "place":
        place_name = input("Enter place name (e.g., 'Sampaloc, Manila'): ").strip()
        coordinates = None
        distance_meters = None
        location = place_name
    else:
        try:
            lat = float(input("Enter latitude (e.g., 14.6514): ").strip())
            lon = float(input("Enter longitude (e.g., 121.0497): ").strip())
            coordinates = (lat, lon)
            location = coordinates
        except ValueError:
            print("Invalid latitude or longitude input.")
            exit(1)

        while True:
            try:
                distance_meters = int(input("Enter search radius in meters (e.g., 2000): ").strip())
                if distance_meters > 0:
                    break
                else:
                    print("Distance must be a positive number.")
            except ValueError:
                print("Please enter a valid number for distance.")

    # Run settings
    total_runs = 1
    successful_runs = 0
    print(f"\nRunning evaluation for {total_runs} runs...")

    for run_num in range(1, total_runs + 1):
        print(f"\n=== Run {run_num}/{total_runs} ===")
        try:
            evaluation(location, distance_meters, ["school", "college", "institute", "university"])
            successful_runs += 1
        except KeyboardInterrupt:
            print("\nUser interrupted the process.")
            break
        except Exception as e:
            print(f"Critical error during run {run_num}: {str(e)}")
            break

    print(f"\nCompleted {successful_runs}/{total_runs} successful runs.")
    if successful_runs > 0:
        print("Check execution_times.csv for results.")
