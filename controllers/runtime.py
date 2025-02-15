import csv
from datetime import datetime

def runtime(graph_type, place_name, odtc_time, tc_time, odtc_nodes_count, tc_nodes_count):
    filename = "execution_times.csv"
    
    # Create file with header if needed
    try:
        with open(filename, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'graph_type', 'place_name', 'odtc_time', 'tc_time', 'odtc_nodes_count', 'tc_nodes_count'])
    except FileExistsError:
        pass
    
    # Append new entry
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            graph_type,
            place_name,
            round(odtc_time, 4),
            round(tc_time, 4),
            odtc_nodes_count,  # New: Number of ODT Central Nodes
            tc_nodes_count     # New: Number of TC Central Nodes
        ])
