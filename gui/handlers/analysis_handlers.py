import io
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from controllers.analyze_runtime import show_results


def run_analysis():
    """
    Calls the runtime analysis function and returns results as a string.
    """


    # Capture printed output
    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    show_results()  # Run analysis

    sys.stdout = sys.__stdout__  # Reset standard output
    return output_buffer.getvalue()  # Return captured text
