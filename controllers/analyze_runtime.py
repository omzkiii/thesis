import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from collections import defaultdict
from scipy.stats import normaltest, ttest_rel, wilcoxon, skew, kurtosis

def read_runtimes_from_csv(filename="execution_times.csv"):
    """
    Reads ODTC and TC runtimes from CSV file and organizes them by graph type.
    Returns:
        dict: {graph_type: (odtc_runtimes list, tc_runtimes list)}
    """
    runtimes = defaultdict(lambda: ([], []))  # Store runtimes by graph type

    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                graph_type = row[1].strip()  # Graph type column
                odtc_runtimes, tc_runtimes = runtimes[graph_type]
                odtc_runtimes.append(float(row[3]))  # ODTC runtime
                tc_runtimes.append(float(row[8]))  # TC runtime
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
            continue  # Skip empty datasets

        # Compute skewness and kurtosis
        odtc_skewness = skew(odtc_runtimes)
        tc_skewness = skew(tc_runtimes)
        odtc_kurtosis = kurtosis(odtc_runtimes)
        tc_kurtosis = kurtosis(tc_runtimes)

        # Perform normality tests using D'Agostino and Pearson's test
        odtc_p_value = normaltest(odtc_runtimes).pvalue if len(odtc_runtimes) >= 3 else None
        tc_p_value = normaltest(tc_runtimes).pvalue if len(tc_runtimes) >= 3 else None

        odtc_normal = odtc_p_value is not None and odtc_p_value > 0.05  # True if ODTC is normally distributed
        tc_normal = tc_p_value is not None and tc_p_value > 0.05  # True if TC is normally distributed

        # Choose the correct statistical test per graph type
        if odtc_normal and tc_normal:
            t_stat, p_value = ttest_rel(odtc_runtimes, tc_runtimes)
            test_used = "Paired t-test"
        else:
            t_stat, p_value = wilcoxon(odtc_runtimes, tc_runtimes)
            test_used = "Wilcoxon signed-rank test"

        # Store results per graph type
        results[graph_type] = {
            "test_used": test_used,
            "t_stat": t_stat,
            "p_value": p_value,
            "mean_odtc": sum(odtc_runtimes) / len(odtc_runtimes),
            "mean_tc": sum(tc_runtimes) / len(tc_runtimes),
            "samples": len(odtc_runtimes),
            "odtc_skewness": odtc_skewness,
            "tc_skewness": tc_skewness,
            "odtc_kurtosis": odtc_kurtosis,
            "tc_kurtosis": tc_kurtosis,
            "odtc_normal": odtc_normal,
            "tc_normal": tc_normal,
            "odtc_p_value": odtc_p_value,
            "tc_p_value": tc_p_value,
        }

    return results  # Dictionary with results for each graph type

def interpret_skewness(value):
    """Returns a textual interpretation of skewness."""
    if value < -0.5:
        return "Left-Skewed"
    elif value > 0.5:
        return "Right-Skewed"
    else:
        return "Approximately Symmetrical"

def interpret_kurtosis(value):
    """Returns a textual interpretation of kurtosis."""
    if value < 3:
        return "Light-Tailed (Platykurtic)"
    elif value > 3:
        return "Heavy-Tailed (Leptokurtic)"
    else:
        return "Normal Tailed (Mesokurtic)"

def show_results():
    try:
        results_by_type = analyze_runtime()

        for graph_type, results in results_by_type.items():
            print(f"\n=== Runtime Analysis for {graph_type} Graph ===")
            print(f"Dataset size: {results['samples']} runs")
            print(f"Average ODTC time: {results['mean_odtc']} seconds")
            print(f"Average TC time: {results['mean_tc']} seconds")

            print(f"Skewness Interpretation:")
            print(f" - ODTC: {interpret_skewness(results['odtc_skewness'])}")
            print(f" - TC: {interpret_skewness(results['tc_skewness'])}")

            print(f"Kurtosis Interpretation:")
            print(f" - ODTC: {interpret_kurtosis(results['odtc_kurtosis'])}")
            print(f" - TC: {interpret_kurtosis(results['tc_kurtosis'])}")

            print(f"Normality Test (D'Agostino-Pearson) Results:")
            print(f" - ODTC p-value: {results['odtc_p_value']} {'(Normal)' if results['odtc_normal'] else '(Not Normal)'}")
            print(f" - TC p-value: {results['tc_p_value']} {'(Normal)' if results['tc_normal'] else '(Not Normal)'}")

            print(f"Statistical test used: {results['test_used']}")
            print(f"P-value: {results['p_value']}")

            if results["p_value"] < 0.05:
                print("Conclusion: Significant difference found (p < 0.05)")
            else:
                print("Conclusion: No significant difference found")

    except FileNotFoundError:
        print("No data found. Run main.py first!")

if __name__ == "__main__":
    show_results()
