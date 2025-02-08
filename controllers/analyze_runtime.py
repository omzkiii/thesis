import csv
from collections import defaultdict
from scipy.stats import shapiro, ttest_rel, wilcoxon

def read_runtimes_from_csv(filename="execution_times.csv"):
    """
    Reads ODTC and TC runtimes from CSV file and organizes them by graph type.
    Returns:
        dict: {graph_type: (odtc_runtimes list, tc_runtimes list)}
    """
    runtimes = defaultdict(lambda: ([], []))  # Dictionary for storing graph-type-separated runtimes
    
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                graph_type = row[1].strip()  # Graph type column
                odtc_runtimes, tc_runtimes = runtimes[graph_type]
                odtc_runtimes.append(float(row[3]))  # ODTC runtime
                tc_runtimes.append(float(row[4]))  # TC runtime
    except FileNotFoundError:
        raise FileNotFoundError(f"Runtime data file {filename} not found. Run evaluations first.")
    
    return runtimes  # Dictionary grouped by graph type

def analyze_runtime(filename="execution_times.csv"):
    """
    Analyzes runtime and performs statistical tests separately for each graph type.
    Returns:
        dict: {graph_type: statistical analysis results}
    """
    # Read data from CSV
    runtimes_by_type = read_runtimes_from_csv(filename)
    
    results = {}
    
    for graph_type, (odtc_runtimes, tc_runtimes) in runtimes_by_type.items():
        if not odtc_runtimes or not tc_runtimes:
            continue  # Skip empty sets

        # Perform normality test
        odtc_normal = shapiro(odtc_runtimes).pvalue > 0.05
        tc_normal = shapiro(tc_runtimes).pvalue > 0.05

        # Choose appropriate statistical test
        if odtc_normal and tc_normal:
            t_stat, p_value = ttest_rel(odtc_runtimes, tc_runtimes)
            test_used = "Paired t-test"
        else:
            t_stat, p_value = wilcoxon(odtc_runtimes, tc_runtimes)
            test_used = "Wilcoxon signed-rank test"

        # Store results
        results[graph_type] = {
            'test_used': test_used,
            't_stat': t_stat,
            'p_value': p_value,
            'mean_odtc': sum(odtc_runtimes) / len(odtc_runtimes),
            'mean_tc': sum(tc_runtimes) / len(tc_runtimes),
            'samples': len(odtc_runtimes)
        }
    
    return results  # Dictionary with results for each graph type

def show_results():
    try:
        results_by_type = analyze_runtime()
        
        for graph_type, results in results_by_type.items():
            print(f"\n=== Runtime Analysis for {graph_type} Graph ===")
            print(f"Dataset size: {results['samples']} runs")
            print(f"Average ODTC time: {results['mean_odtc']:.10f} seconds")
            print(f"Average TC time: {results['mean_tc']:.10f} seconds")
            print(f"Statistical test: {results['test_used']}")
            print(f"P-value: {results['p_value']}")
            if results['p_value'] < 0.05:
                print("Conclusion: Significant difference found (p < 0.05)")
            else:
                print("Conclusion: No significant difference found")
    
    except FileNotFoundError:
        print("No data found. Run main.py first!")

if __name__ == "__main__":
    show_results()
