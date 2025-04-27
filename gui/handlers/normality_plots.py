import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import tkinter as tk
from controllers.analyze_runtime import read_runtimes_from_csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NormalityPlotNavigator:
    def __init__(self, root, runtimes_by_type):
        self.root = root
        self.runtimes_by_type = list(runtimes_by_type.items())  # Convert dictionary to list for indexing
        self.current_index = 0  # Track current graph type
        self.fig = None  # Store figure reference

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_plot)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_plot)
        self.next_button.pack(side=tk.RIGHT, padx=5)

        self.update_plot()

    def update_plot(self):
        """Generate and display the normality plot for the current graph type."""
        if self.fig:
            for widget in self.canvas_frame.winfo_children():
                widget.destroy()  # Clear previous plot

        graph_type, (odtc_runtimes, tc_runtimes) = self.runtimes_by_type[self.current_index]

        if not odtc_runtimes or not tc_runtimes:
            return

        self.fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        self.fig.suptitle(f"Normality Test for {graph_type} Graph", fontsize=14)

        # --- Histogram for ODTC ---
        sns.histplot(odtc_runtimes, kde=True, bins=20, ax=axes[0, 0])
        axes[0, 0].set_title("ODTC Runtime Histogram")
        axes[0, 0].set_xlabel("Execution Time")
        axes[0, 0].set_ylabel("Frequency")

        # --- Q-Q Plot for ODTC ---
        stats.probplot(odtc_runtimes, dist="norm", plot=axes[0, 1])
        axes[0, 1].set_title("ODTC Q-Q Plot")

        # --- Histogram for TC ---
        sns.histplot(tc_runtimes, kde=True, bins=20, ax=axes[1, 0])
        axes[1, 0].set_title("TC Runtime Histogram")
        axes[1, 0].set_xlabel("Execution Time")
        axes[1, 0].set_ylabel("Frequency")

        # --- Q-Q Plot for TC ---
        stats.probplot(tc_runtimes, dist="norm", plot=axes[1, 1])
        axes[1, 1].set_title("TC Q-Q Plot")

        plt.tight_layout(rect=[0, 0, 1, 0.95])

        canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def next_plot(self):
        """Show the next graph type."""
        if self.current_index < len(self.runtimes_by_type) - 1:
            self.current_index += 1
            self.update_plot()

    def prev_plot(self):
        """Show the previous graph type."""
        if self.current_index > 0:
            self.current_index -= 1
            self.update_plot()


def generate_normality_plots():
    """Creates a Tkinter window for normality test navigation."""
    runtimes_by_type = read_runtimes_from_csv("execution_times2.csv")

    if not runtimes_by_type:
        print("No runtime data found!")
        return

    root = tk.Toplevel()
    root.title("Normality Test Navigation")
    root.geometry("800x600")

    NormalityPlotNavigator(root, runtimes_by_type)

    root.mainloop()


if __name__ == "__main__":
    generate_normality_plots()
