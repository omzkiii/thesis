from controllers.select_subgraph import select_subgraph_benchmark
from controllers.get_subgraph import get_subgraph_benchmark
from controllers.get_graph import get_graph
import csv

amenities = ["school", "college", "institute", "university"]


def subgraph_comparison(loc, distance=None):
    graph, nodes, edges, landmarks = get_graph(
        loc, distance=distance, amenities=amenities
    )
    select_subgraph_runtime = select_subgraph_benchmark(graph, nodes, landmarks)
    get_subgraph_runtime = get_subgraph_benchmark(graph, nodes, landmarks)

    filename = "subgraph_execution_times.csv"

    try:
        with open(filename, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["place", "odtc_subgraph", "tc_subgraph"])
    except FileExistsError:
        pass

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([loc, select_subgraph_runtime, get_subgraph_runtime])


if __name__ == "__main__":
    graph, nodes, edges, landmarks = get_graph(
        "Sampaloc, Manila", distance=None, amenities=amenities
    )
    for _ in range(10):
        select_subgraph_runtime = select_subgraph_benchmark(graph, nodes, landmarks)
        print("========SELECT==========")
        print(select_subgraph_runtime)
        print("========================")
        # get_subgraph_runtime = get_subgraph_benchmark(graph, nodes, landmarks)
        # print("==========GET===========")
        # print(get_subgraph_runtime)
        # print("========================")
