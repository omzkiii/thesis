import osmnx as ox
import networkx as nx


def get_graph(center_point, distance, amenities):
    graph = ox.graph_from_point(
        center_point,
        dist=distance,
        network_type="drive",
        custom_filter='["highway"~"primary|primary_link|secondary|secondary_link|tertiary|tertiary_link"]',
    )

    largest_scc = max(nx.strongly_connected_components(graph), key=len)
    graph = graph.subgraph(largest_scc).copy()

    nodes, edges = ox.graph_to_gdfs(graph)

    landmarks = ox.features_from_point(
        center_point, tags={"amenity": amenities}, dist=distance
    )

    return graph, nodes, edges, landmarks


if __name__ == "__main__":
    # Example usage for Sampaloc, Manila coordinates
    coordinates = (14.6197, 121.0053)  # Latitude, Longitude
    distance_meters = 1000  # 2km radius

    graph, nodes, edges, landmarks = get_graph(
        coordinates, distance_meters, ["school", "college", "institute", "university"]
    )

