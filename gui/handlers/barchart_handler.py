import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def generate_barchart(df_melted, graph_type, parent_frame):
    """Creates and embeds a Bar Chart in the GUI."""
    figure, ax = plt.subplots(figsize=(8, 6))

    mean_runtime = df_melted.groupby("Algorithm")["Runtime"].mean().reset_index()
    sns.barplot(x="Algorithm", y="Runtime", data=mean_runtime, ax=ax)
    
    ax.set_title(f"{graph_type} - Mean Runtime")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel("Runtime (seconds)")

    canvas = FigureCanvasTkAgg(figure, master=parent_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    toolbar = NavigationToolbar2Tk(canvas, parent_frame)
    toolbar.update()
    toolbar.pack(side="bottom", fill="x")

    canvas.draw()
