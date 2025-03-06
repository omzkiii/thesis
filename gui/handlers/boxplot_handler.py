import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def generate_boxplot(df_melted, graph_type, parent_frame):
    """Creates and embeds a Box Plot in the GUI."""
    figure, ax = plt.subplots(figsize=(8, 6))
    
    sns.boxplot(x="Algorithm", y="Runtime", data=df_melted, ax=ax)
    ax.set_title(f"{graph_type} - Runtime Distribution")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel("Runtime (seconds)")

    canvas = FigureCanvasTkAgg(figure, master=parent_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    toolbar = NavigationToolbar2Tk(canvas, parent_frame)
    toolbar.update()
    toolbar.pack(side="bottom", fill="x")

    canvas.draw()
