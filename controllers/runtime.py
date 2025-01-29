import csv
from datetime import datetime

def runtime(odtc_time, tc_time):
    filename = "execution_times.csv"
    
    # Create file with header if needed
    try:
        with open(filename, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'odtc_time', 'tc_time'])
    except FileExistsError:
        pass
    
    # Append new entry
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            round(odtc_time, 4),
            round(tc_time, 4)
        ])

