from get_graph import get_graph
from gui import gui
from construct_graph import construct_graph
from evaluate import evaluate
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc


def generate(place_name, amenities):
    filename = f"{place_name} - {amenities[0]}"
    graph, nodes, edges, landmarks = get_graph(place_name, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    terminal_nodes = odtc(subgraphs)
    # terminal_nodes = random.sample(list(graph.nodes), 10)
    route = steiner_network(graph, nodes, edges, terminal_nodes)
    construct_graph(nodes, edges, subgraphs, landmarks, terminal_nodes, route, filename)


def evaluation(place_name, amenities):
    graph, nodes, edges, landmarks = get_graph(place_name, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    odtc(subgraphs)
    # tc()
    # evaluate()


if __name__ == "__main__":
    gui(generate)

    # class App(tkinter.Frame):
    #     def __init__(self, master):
    #         super().__init__(master)
    #         self.pack()
    #
    #         self.entrythingy = tkinter.Entry()
    #         self.entrythingy.pack()
    #
    #         # Create the application variable.
    #         self.contents = tkinter.StringVar()
    #         # Set it to some value.
    #         self.contents.set("this is a variable")
    #         # Tell the entry widget to watch this variable.
    #         self.entrythingy["textvariable"] = self.contents
    #
    #         # Define a callback for when the user hits return.
    #         # It prints the current value of the variable.
    #         self.entrythingy.bind("<Key-Return>", self.print_contents)
    #
    #     def print_contents(self, event):
    #         print("Hi. The current entry content is:", self.contents.get())
    #
    # root = Tk()
    # # frm = ttk.Frame(root, padding=10)
    # # frm.grid()
    # # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    # # btn = ttk.Button(frm, text="Quit", command=root.destroy)
    # # btn.grid(column=0, row=1)
    # # print(btn.configure().keys())
    # myapp = App(root)
    # root.mainloop()
    # generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
    # evaluation("Sampaloc, Manila", ["school", "college", "institute", "university"])
