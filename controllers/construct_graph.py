import osmnx as ox
import folium
import numpy as np

legend_html = """
    <div style="
        position: absolute;
        bottom: 100px;
        left: 50px;
        width: 250px;
        height: 300px;
        background-color: white;
        z-index:9999;
        font-size:24px;
        border-radius: 5px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    ">
        <b>Legend</b><br>
        Landmark <i style="background:blue; width:20px; height:20px; display:inline-block;"></i><br>
        Route <i style="background:red; width:70px; height:10px; display:inline-block;"></i><br>
        Central Node <i style="background:yellow; width:20px; height:20px; border-radius:100%; display:inline-block;"></i><br>
        Path <i style="background:blue; width:50px; height:5px; display:inline-block;"></i><br>
        Junction <i style="background:purple; width:10px; height:10px; border-radius:100%; display:inline-block;"></i><br>
    </div>
    """


def construct_graph(
    nodes, edges, subgraphs, landmarks, terminal_nodes, route, filename
):
    # nodes, edges = ox.graph_to_gdfs(graph, nodes=True)

    base_map = edges.explore(
        # column="highway",
        tooltip=["name", "highway", "length"],
        tiles="CartoDB positron",
    )
    for _, r in route.iterrows():
        if r.get("oneway", False):
            coords = list(r.geometry.coords)
            mid_idx = len(coords) // 2
            lon1, lat1 = coords[0]
            lon2, lat2 = coords[-1]

            bearing = ox.bearing.calculate_bearing(lat1, lon1, lat2, lon2)

            folium.Marker(
                location=[coords[mid_idx][1], coords[mid_idx][0]],  # (lat, lon)
                icon=folium.DivIcon(
                    html=f"""
                    <div style="
                        transform: rotate({bearing}deg);
                        font-size: 24px;
                        color: red;
                    ">↑</div>
                """
                ),
            ).add_to(base_map)

    landmarks_map = landmarks.explore(
        m=base_map,
        color="blue",
        marker_kwds={"radius": 5},
        tooltip="name",
        popup=True,
    )

    junction_map = nodes.explore(
        m=landmarks_map,
        color="purple",
        tooltip=["osmid", "street_count"],
        marker_kwds={"radius": 3},
        tiles="CartoDB positron",
    )

    route_map = route.explore(
        m=junction_map,
        color="red",
        style={"weight": 5, "color": "red"},
        marker_kwds={"radius": 1},
        tiles="CartoDB positron",
    )

    terminal = nodes[nodes.index.isin(terminal_nodes)]

    catchment_map = terminal.explore(
        m=route_map,
        color="yellow",
        marker_kwds={"radius": 10},
        tooltip=["osmid", "street_count"],
        popup=False,
    )
    catchment_map.get_root().html.add_child(folium.Element(legend_html))
    catchment_map.save(f"{filename}.html")


if __name__ == "__main__":
    print("Constructing Graph")
