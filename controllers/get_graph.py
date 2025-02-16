import osmnx as ox
import networkx as nx

def get_graph(location, distance=None, amenities=None):
    """
    Fetch a graph and landmarks from OSM based on a location, which can be either:
    - A place name (string)
    - A tuple of coordinates (latitude, longitude)
    
    Parameters:
        location (str or tuple): A place name or a coordinate tuple (lat, lon).
        distance (int, optional): The search radius in meters if using coordinates.
        amenities (list, optional): List of amenities to fetch.
    
    Returns:
        tuple: graph, nodes, edges, landmarks
    """
    
    if isinstance(location, str):  # If location is a place name
        graph = ox.graph_from_place(
            location,
            network_type="drive",
            custom_filter='["highway"~"primary|primary_link|secondary|secondary_link|tertiary|tertiary_link"]',
        )
        landmarks = ox.features_from_place(
            location,
            tags={"amenity": amenities} if amenities else {},
        )
    
    elif isinstance(location, tuple) and len(location) == 2:  # If location is coordinates (lat, lon)
        if distance is None:
            raise ValueError("A distance parameter is required when using coordinates.")
        
        graph = ox.graph_from_point(
            location,
            dist=distance,
            network_type="drive",
            custom_filter='["highway"~"primary|primary_link|secondary|secondary_link|tertiary|tertiary_link"]',
        )
        landmarks = ox.features_from_point(
            location,
            tags={"amenity": amenities} if amenities else {},
            dist=distance
        )
    
    else:
        raise ValueError("Invalid location format. Must be a place name (str) or coordinates (lat, lon) tuple.")
    
    # Get the largest strongly connected component
    largest_scc = max(nx.strongly_connected_components(graph), key=len)
    graph = graph.subgraph(largest_scc).copy()
    
    # Convert to GeoDataFrames
    nodes, edges = ox.graph_to_gdfs(graph)
    
    return graph, nodes, edges, landmarks

if __name__ == "__main__":
    pass