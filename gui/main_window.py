import tkinter as tk
from tkinter import Button, Text, Scrollbar, Frame, Toplevel
from handlers.analysis_handlers import run_analysis
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class PageSwitcher:
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


def main_window():
    root = tk.Tk()
    root.title("Network Analysis GUI")
    root.geometry("300x150")

    Button(root, text="Open Analysis Window", command=analyze_runtime_window).pack(
        pady=10
    )
    Button(root, text="Open Box Plot Window", command=plot_runtime_boxplot_window).pack(
        pady=10
    )

    root.mainloop()


def analyze_runtime_window():
    analysis_window = Toplevel()
    analysis_window.title("Runtime Analysis Results")

    result_text = Text(analysis_window, height=15, width=80, wrap="word")
    result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(analysis_window, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)

    results = run_analysis()
    result_text.insert(tk.END, results)


def plot_runtime_boxplot_window():
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
        plot_window.title("Box Plot Analysis")

        plot_frame = Frame(plot_window)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for graph_type in graph_types:
            graph_sub_frame = Frame(plot_frame)
            frames.append(graph_sub_frame)

            label = tk.Label(
                graph_sub_frame,
                text=f"Box Plot - {graph_type} Graph",
                font=("Arial", 12, "bold"),
            )
            label.pack()

            figure, ax = plt.subplots(figsize=(8, 6))
            canvas = FigureCanvasTkAgg(figure, master=graph_sub_frame)
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            # Add Navigation Toolbar for Zoom and Pan
            toolbar = NavigationToolbar2Tk(canvas, graph_sub_frame)
            toolbar.update()
            toolbar.pack(side=tk.BOTTOM, fill=tk.X)

            df_filtered = df[df["Graph Type"] == graph_type]
            df_melted = df_filtered.melt(
                id_vars=["Graph Type"],
                value_vars=["ODTC Runtime", "TC Runtime"],
                var_name="Algorithm",
                value_name="Runtime",
            )

            sns.boxplot(x="Algorithm", y="Runtime", data=df_melted, ax=ax)
            ax.set_title(f"{graph_type} Graph")
            ax.set_xlabel("Algorithm")
            ax.set_ylabel("Runtime (seconds)")

            canvas.draw()

        switcher = PageSwitcher(plot_frame, frames)

        nav_frame = Frame(plot_window)
        nav_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        Button(nav_frame, text="Previous", command=switcher.prev_page).pack(
            side=tk.LEFT, padx=5
        )
        Button(nav_frame, text="Next", command=switcher.next_page).pack(
            side=tk.RIGHT, padx=5
        )

    except FileNotFoundError:
        print("CSV file not found. Make sure execution_times.csv is available.")
    except Exception as e:
        print(f"Error generating plot: {e}")


if __name__ == "__main__":
    main_window()
