import json
import requests
import osmnx as ox
from shapely.geometry import LineString, Polygon, Point
from shapely.ops import unary_union

# from geopy.distance import geodesic
# from IPython.display import display


def get_sampaloc_boundary():
    sampaloc = ox.geocode_to_gdf("Sampaloc, Manila, Philippines", which_result=1)
    if sampaloc.empty:
        raise ValueError("Could not find Sampaloc boundary.")
    return sampaloc.loc[0, "geometry"]


relation_ids_with_names = [
    (15021432, "Pasig - Quiapo Via Commonwealth"),
    (11370053, "Balic-Balic - Quiapo via Lepanto"),
    (11370052, "Balic-Balic → Bustillos via G. Tuazon"),
    (11613213, "lardizabal - rizal avenue via m. dela fuente"),
    (11613219, "Balic-Balic → España/M. dela Fuente"),
    (11246068, "Quiapo → Punta via Santa Mesa"),
    (11291811, "Lealtad - Quiapo (Barbosa) via Lepanto"),
    (11613216, "Gastambide - Divisoria via Morayta"),
]


def count_nodes_edges(trimmed_segments):
    nodes = set()
    edges = 0

    for segment in trimmed_segments:
        coords = list(segment.coords)  # Extract coordinates from LineString
        nodes.update(coords)  # Add nodes to the set
        edges += len(coords) - 1  # Each segment between two nodes is an edge

    return len(nodes), edges


def get_sampaloc():
    graph = ox.graph_from_place(
        "Sampaloc, Manila",
        network_type="drive",
        custom_filter='["highway"~"primary|primary_link|secondary|secondary_link|tertiary|tertiary_link"]',
    )
    nodes, edges = ox.graph_to_gdfs(graph)

    sampaloc_edges = []
    sampaloc_nodes = [node for node, _ in nodes.iterrows()]

    for _, edge in edges.iterrows():
        if isinstance(edge["osmid"], list):
            # sampaloc_edges = sampaloc_edges + edge["osmid"]
            sampaloc_edges.extend(edge["osmid"])
        else:
            sampaloc_edges.append(edge["osmid"])

    return sampaloc_nodes, sampaloc_edges


def get_data_jeepney():
    s_nodes, s_edges = get_sampaloc()
    boundary = get_sampaloc_boundary()
    ways = []
    data = {}
    paths = {}
    for idx, (relation_id, name) in enumerate(relation_ids_with_names):
        overpass_url = "http://overpass-api.de/api/interpreter"
        query = f"""
            [out:json];
            relation({relation_id});
            (._;>>;);
            out geom;
            """
        response = requests.get(overpass_url, params={"data": query})
        response.raise_for_status()

        data = response.json()
        elements = data.get("elements", [])
        ways = [el["id"] for el in elements if el["type"] == "way" and "geometry" in el]
        point = [el["id"] for el in elements if el["type"] == "node"]
        s_point = [p for p in point if p in s_nodes]
        s_ways = [s for s in ways if s in s_edges]
        # print(f"{name}: nodes= {len(s_point)} edges={len(s_ways)}")
        print(name, s_ways)

        # trimmed_segments = []
        # for way in ways:
        #     coordinates = [(point["lat"], point["lon"]) for point in way["geometry"]]
        #     route_line = LineString([(lon, lat) for lat, lon in coordinates])
        #     trimmed_route = route_line.intersection(boundary)
        #     if trimmed_route.is_empty:
        #         continue
        #
        #     if trimmed_route.geom_type == "MultiLineString":
        #         trimmed_segments = trimmed_segments + list(trimmed_route.geoms)
        #     else:
        #         trimmed_segments = trimmed_segments + [trimmed_route]
        #
        # n, e = count_nodes_edges(trimmed_segments)
        # print(f"{name}: Nodes= {n}, Edges= {e}")

        # ways = [el for el in elements]
        # ways = [el["type"] for el in elements]

        # total_distance = 0
    # with open("jeepney_routes.json", "w") as file:
    #     json.dump(paths, file, indent=4)
    # print(json.dumps(paths))


# with open("sampaloc_boundary.json", "w") as file:
#     json.dump(sampaloc_data, file, indent=4)
# print([node for node, _ in nodes.iterrows()])
get_data_jeepney()
