import osmnx as ox
import networkx as nx


def get_graph(place_name, amenities):
    graph = ox.graph_from_place(
        place_name,
        network_type="drive",
        custom_filter='["highway"~"primary|primary_link|secondary|secondary_link|tertiary|tertiary_link"]',
    )

    largest_scc = max(nx.strongly_connected_components(graph), key=len)
    graph = graph.subgraph(largest_scc).copy()

    nodes, edges = ox.graph_to_gdfs(graph)

    landmarks = ox.features_from_place(
        place_name,
        tags={"amenity": amenities},
    )

    return graph, nodes, edges, landmarks


if __name__ == "__main__":
    get_graph("Sampaloc, Manila", ["school", "college", "institute", "university"])
