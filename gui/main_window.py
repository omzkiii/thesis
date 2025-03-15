import tkinter as tk
from tkinter import Button, Frame, Toplevel, Text, Scrollbar
import pandas as pd
from handlers.boxplot_handler import generate_boxplot
from handlers.barchart_handler import generate_barchart
from handlers.analysis_handlers import run_analysis
from handlers.route_handler import launch_route_generator
from handlers.normality_plots import generate_normality_plots


class PageSwitcher:
    """Handles switching between pages for different graph types."""
    def __init__(self, parent, frames):
        self.parent = parent
        self.frames = frames
        self.current_index = 0
        self.show_frame(self.current_index)

    def show_frame(self, index):
        for frame in self.frames:
            frame.pack_forget()
        self.frames[index].pack(fill=tk.BOTH, expand=True)

    def next_page(self):
        if self.current_index < len(self.frames) - 1:
            self.current_index += 1
            self.show_frame(self.current_index)

    def prev_page(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_frame(self.current_index)


def analyze_runtime_window():
    """Creates a window for runtime analysis results."""
    analysis_window = Toplevel()
    analysis_window.title("Runtime Analysis Results")

    result_text = Text(analysis_window, height=15, width=80, wrap="word")
    result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(analysis_window, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)

    results = run_analysis()
    result_text.insert(tk.END, results)


def plot_runtime_window():
    """Creates GUI window with box plots and bar charts for runtime analysis."""
    try:
        csv_file_path = "execution_times.csv"
        df = pd.read_csv(csv_file_path)
        df.columns = df.columns.str.strip()
        df = df.rename(
            columns={
                "graph_type": "Graph Type",
                "odtc_time": "ODTC Runtime",
                "tc_time": "TC Runtime",
            }
        )

        graph_types = df["Graph Type"].unique()
        frames = []

        plot_window = Toplevel()
        plot_window.title("Runtime Analysis")

        plot_frame = Frame(plot_window)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for graph_type in graph_types:
            df_filtered = df[df["Graph Type"] == graph_type]
            df_melted = df_filtered.melt(id_vars=["Graph Type"], value_vars=["ODTC Runtime", "TC Runtime"],
                                         var_name="Algorithm", value_name="Runtime")

            for plot_type in ["Box Plot", "Bar Chart"]:
                graph_sub_frame = Frame(plot_frame)
                frames.append(graph_sub_frame)

                label = tk.Label(graph_sub_frame, text=f"{plot_type} - {graph_type} Graph", font=("Arial", 12, "bold"))
                label.pack()

                if plot_type == "Box Plot":
                    generate_boxplot(df_melted, graph_type, graph_sub_frame)
                else:
                    generate_barchart(df_melted, graph_type, graph_sub_frame)

        switcher = PageSwitcher(plot_frame, frames)

        nav_frame = Frame(plot_window)
        nav_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        Button(nav_frame, text="Previous", command=switcher.prev_page).pack(side=tk.LEFT, padx=5)
        Button(nav_frame, text="Next", command=switcher.next_page).pack(side=tk.RIGHT, padx=5)

    except FileNotFoundError:
        print("CSV file not found. Make sure execution_times.csv is available.")
    except Exception as e:
        print(f"Error generating plot: {e}")


def show_normality_test():
    """Triggers the normality test plots."""
    generate_normality_plots()


def main_window():
    """Main Tkinter GUI window."""
    root = tk.Tk()
    root.title("Network Analysis GUI")
    root.geometry("300x250")

    Button(root, text="Open Analysis Window", command=analyze_runtime_window).pack(pady=5)
    Button(root, text="Open Runtime Analysis", command=plot_runtime_window).pack(pady=5)
    Button(root, text="Generate Route", command=launch_route_generator).pack(pady=5)
    Button(root, text="Show Normality Test", command=show_normality_test).pack(pady=5)  # ✅ NEW BUTTON ADDED

    root.mainloop()


if __name__ == "__main__":
    main_window()
