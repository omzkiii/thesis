from get_graph import get_graph
from construct_graph import construct_graph
from evaluate import evaluate
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc


def generate(place_name, amenities):
    nodes, edges, landmarks = get_graph(place_name, amenities)
    # service_nodes, catchment_nodes = select_subgraph(nodes, landmarks)
    select_subgraph(nodes, landmarks)
    odtc()
    steiner_network()
    # construct_graph(nodes, edges, landmarks, service_nodes, catchment_nodes)


def evaluation(place_name, amenities):
    nodes, edges, landmarks = get_graph(place_name, amenities)
    service_nodes, catchment_nodes = select_subgraph(nodes, landmarks)
    odtc()
    tc()
    steiner_network()
    evaluate()


if __name__ == "__main__":
    generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
