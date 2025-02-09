import osmnx as ox


def construct_graph(nodes, edges, subgraphs, landmarks, terminal_nodes, route):
    # nodes, edges = ox.graph_to_gdfs(graph, nodes=True)

    base_map = edges.explore(
        # column="highway",  # Color edges based on highway type
        tooltip=["name", "highway", "length"],  # Tooltip for edges
        tiles="CartoDB positron",  # Use a clean basemap
    )

    landmarks_map = landmarks.explore(
        m=base_map,  # Add to the base map
        color="blue",  # Color for POIs
        marker_kwds={"radius": 5},  # Marker size
        tooltip="name",  # Tooltip for POI names
        popup=True,  # Enable popups for POIs
    )

    junction_map = nodes.explore(
        m=landmarks_map,
        color="purple",  # Node color for junctions
        tooltip=["osmid", "street_count"],  # Tooltip for junction details
        marker_kwds={"radius": 3},  # Marker size
        tiles="CartoDB positron",  # Basemap style
    )

    route_map = route.explore(
        m=junction_map,
        color="red",
        style={"weight": 10, "color": "red"},
        marker_kwds={"radius": 10},  # Marker size
        tiles="CartoDB positron",  # Basemap style
    )

    # print(subgraphs)
    terminal = nodes[nodes.index.isin(terminal_nodes)]

    catchment_map = terminal.explore(
        m=route_map,
        color="yellow",  # Highlight nodes near POIs in green
        marker_kwds={"radius": 10},  # Marker size
        tooltip=["osmid", "street_count"],  # Tooltip for node details
        popup=False,  # Disable popups for nodes
    )

    catchment_map.save("test2.html")

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
