import csv
from scipy.stats import shapiro, ttest_rel, wilcoxon

def read_runtimes_from_csv(filename="execution_times.csv"):
    """
    Read ODTC and TC runtimes from CSV file.
    Returns:
        tuple: (odtc_runtimes list, tc_runtimes list)
    """
    odtc_runtimes = []
    tc_runtimes = []
    
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                odtc_runtimes.append(float(row[1]))
                tc_runtimes.append(float(row[2]))
    except FileNotFoundError:
        raise FileNotFoundError(f"Runtime data file {filename} not found. Run evaluations first.")
    
    return odtc_runtimes, tc_runtimes

def analyze_runtime(filename="execution_times.csv"):
    """
    Analyze runtime and perform statistical tests using data from CSV.
    Returns:
        dict: Statistical test results and runtime analysis
    """
    # Read data from CSV
    odtc_runtimes, tc_runtimes = read_runtimes_from_csv(filename)
    
    results = {}
    
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
    results['test_used'] = test_used
    results['t_stat'] = t_stat
    results['p_value'] = p_value
    results['mean_odtc'] = sum(odtc_runtimes) / len(odtc_runtimes)
    results['mean_tc'] = sum(tc_runtimes) / len(tc_runtimes)
    results['samples'] = len(odtc_runtimes)
    
    return results

def show_results():
    try:
        results = analyze_runtime()
        print("\n=== Runtime Analysis ===")
        print(f"Dataset size: {results['samples']} runs")
        print(f"Average ODTC time: {results['mean_odtc']:.2f} seconds")
        print(f"Average TC time: {results['mean_tc']:.2f} seconds")
        print(f"Statistical test: {results['test_used']}")
        print(f"P-value: {results['p_value']:.4f}")
        if results['p_value'] < 0.05:
            print("Conclusion: Significant difference found (p < 0.05)")
        else:
            print("Conclusion: No significant difference found")
    except FileNotFoundError:
        print("No data found. Run main.py first!")

if __name__ == "__main__":
    show_results()