import csv
from datetime import datetime


def runtime(
    graph_type,
    place_name,
    odtc_time,
    odtc_central_nodes_count,
    total_origin_nodes,
    total_dest_nodes,
    total_odtc_nodes,
    tc_time,
    tc_central_nodes_count,
    total_tc_nodes,
):
    filename = "execution_times_rev.csv"

    # Create file with header if needed
    try:
        with open(filename, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "timestamp",
                    "graph_type",
                    "place_name or coordinates",
                    "odtc_time",
                    "odtc_central_nodes_count",
                    "total_origin_nodes",
                    "total_dest_nodes",
                    "total_odtc_nodes",
                    "tc_time",
                    "tc_central_nodes_count",
                    "total_tc_nodes",
                ]
            )
    except FileExistsError:
        pass

    # Append new entry
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                datetime.now().isoformat(),
                graph_type,
                place_name,
                round(odtc_time, 8),
                odtc_central_nodes_count,  # New: Number of ODT Central Nodes
                total_origin_nodes,
                total_dest_nodes,
                total_odtc_nodes,
                round(tc_time, 8),
                tc_central_nodes_count,  # New: Number of TC Central Nodes
                total_tc_nodes,
            ]
        )
