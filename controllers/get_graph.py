import osmnx as ox
import geopandas as gpd


def get_graph(place_name, amenities):
    # Set the place name
    # place_name = "SAMPALOC, Manila"

    # Download the graph network for the given place
    graph = ox.graph_from_place(place_name, network_type="drive")

    # Convert graph to GeoDataFrames
    nodes, edges = ox.graph_to_gdfs(graph, nodes=True)

    # Fetch POIs for schools, colleges, hospitals, parks, etc.
    landmarks = ox.features_from_place(
        place_name,
        # tags={"amenity": ["school", "college", "institute", "university"]},
        tags={"amenity": amenities},
    )

    nodes_gdf = gpd.GeoDataFrame(
        nodes, geometry=gpd.points_from_xy(nodes["x"], nodes["y"])
    )

    print(landmarks["name"])

    return nodes, edges, landmarks


if __name__ == "__main__":
    get_graph("Sampaloc, Manila", ["school", "college", "institute", "university"])
