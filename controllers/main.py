from get_graph import get_graph
from construct_graph import construct_graph
from evaluate import evaluate
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc
import random
from tkinter import *
from tkinter import ttk


def generate(place_name, amenities):
    graph, nodes, edges, landmarks = get_graph(place_name, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    # terminal_nodes = odtc(subgraphs)
    terminal_nodes = random.sample(list(graph.nodes), 10)
    route = steiner_network(graph, nodes, edges, terminal_nodes)
    construct_graph(nodes, edges, subgraphs, landmarks, terminal_nodes, route)


def evaluation(place_name, amenities):
    graph, nodes, edges, landmarks = get_graph(place_name, amenities)
    subgraphs = select_subgraph(graph, nodes, landmarks)
    odtc(subgraphs)
    # tc()
    # evaluate()


if __name__ == "__main__":
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    btn = ttk.Button(frm, text="Quit", command=root.destroy)
    btn.grid(column=0, row=1)
    print(btn.configure().keys())
    root.mainloop()
    # generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
    # evaluation("Sampaloc, Manila", ["school", "college", "institute", "university"])
