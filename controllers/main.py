from get_graph import get_graph
from construct_graph import construct_graph
from evaluate import evaluate
from odtc import odtc
from select_subgraph import select_subgraph
from steiner_network import steiner_network
from tc import tc


def generate(place_name, ameneties):
    get_graph(place_name, ameneties)
    select_subgraph()
    odtc()
    steiner_network()
    construct_graph()


# def evaluation():
#     identify_service_nodes()
#     select_catchment()
#     odtc()
#     tc()
#     steiner_network()
#     evaluate()


if __name__ == "__main__":
    generate("Sampaloc, Manila", ["school", "college", "institute", "university"])
    # evaluation()
