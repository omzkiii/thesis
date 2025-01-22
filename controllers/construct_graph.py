import osmnx as ox


def construct_graph(nodes, edges, subgraphs):
    # nodes, edges = ox.graph_to_gdfs(graph, nodes=True)

    base_map = edges.explore(
        # column="highway",  # Color edges based on highway type
        tooltip=["name", "highway", "length"],  # Tooltip for edges
        tiles="CartoDB positron",  # Use a clean basemap
    )

    ## TESTER ONLY ---------------

    catchment = subgraphs.get("University of Manila (Main)")[0]
    service = subgraphs.get("University of Manila (Main)")[1]
    landmark = subgraphs.get("University of Manila (Main)")[2]

    landmarks_map = landmark.explore(
        m=base_map,  # Add to the base map
        color="blue",  # Color for POIs
        marker_kwds={"radius": 8},  # Marker size
        tooltip="name",  # Tooltip for POI names
        popup=True,  # Enable popups for POIs
    )

    service_map = service.explore(
        m=landmarks_map,
        color="green",  # Highlight nodes near POIs in green
        marker_kwds={"radius": 10},  # Marker size
        tooltip=["osmid", "street_count"],  # Tooltip for node details
        popup=False,  # Disable popups for nodes
    )

    catchment_map = catchment.explore(
        m=service_map,
        color="yellow",  # Highlight nodes near POIs in green
        marker_kwds={"radius": 10},  # Marker size
        tooltip=["osmid", "street_count"],  # Tooltip for node details
        popup=False,  # Disable popups for nodes
    )
    catchment_map.save("test.html")

    ## TESTER END --------------

    # landmarks_map = landmarks.explore(
    #     m=base_map,  # Add to the base map
    #     color="blue",  # Color for POIs
    #     marker_kwds={"radius": 8},  # Marker size
    #     tooltip="name",  # Tooltip for POI names
    #     popup=True,  # Enable popups for POIs
    # )
    #
    # junctions = nodes[nodes["street_count"] > 1]
    # junction_map = junctions.explore(
    #     m=landmarks_map,
    #     color="red",  # Node color for junctions
    #     tooltip=["osmid", "street_count"],  # Tooltip for junction details
    #     marker_kwds={"radius": 3},  # Marker size
    #     tiles="CartoDB positron",  # Basemap style
    # )
    #
    # service_map = service_nodes.explore(
    #     m=junction_map,
    #     color="green",  # Highlight nodes near POIs in green
    #     marker_kwds={"radius": 10},  # Marker size
    #     tooltip=["osmid", "street_count"],  # Tooltip for node details
    #     popup=False,  # Disable popups for nodes
    # )
    # final_map = catchment_nodes.explore(
    #     m=service_map,
    #     color="yellow",  # Highlight nodes near POIs in green
    #     marker_kwds={"radius": 7},  # Marker size
    #     tooltip=["osmid", "street_count"],  # Tooltip for node details
    #     popup=False,  # Disable popups for nodes
    # )

    # final_map.save("result.html")


if __name__ == "__main__":
    print("Constructing Graph")
