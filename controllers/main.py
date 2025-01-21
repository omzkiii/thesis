from get_graph import get_graph
from construct_graph import construct_graph
from evaluate import evaluate
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc


def generate(place_name, amenities):
    get_graph(place_name, amenities)
    select_subgraph()
    odtc()
    steiner_network()
    construct_graph()


def evaluation(place_name, amenities):
    get_graph(place_name, amenities)
    select_subgraph()
    odtc()
    tc()
    steiner_network()
    evaluate()


if __name__ == "__main__":
    generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
