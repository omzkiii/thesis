from controllers.get_graph import get_graph
from controllers.select_subgraph import select_subgraph
from controllers.odtc import odtc
from controllers.tc import tc

amenities = ["school", "college", "institute", "university"]


def display_central(name, loc, distance=None, amenities=amenities):
    odtc_name = f"{name} - odtc"
    tc_name = f"{name} - tc"
    graph, nodes, edges, landmarks = get_graph(
        loc, distance=distance, amenities=amenities
    )
    print("DONE SELECTING GETTING GRAPH")
    subgraphs = select_subgraph(graph, nodes, landmarks)
    print("DONE SELECTING SUBGRAPH")
    odtc_terminal = odtc(subgraphs)
    print("DONE ODTC")
    tc_terminal = tc(subgraphs)
    print("DONE TC")
    constructGraph(nodes, edges, landmarks, odtc_terminal[0], odtc_name)
    constructGraph(nodes, edges, landmarks, tc_terminal[0], tc_name)


def constructGraph(nodes, edges, landmarks, terminal_nodes, filename):

    base_map = edges.explore(
        tooltip=["name", "highway", "length"],
        tiles="CartoDB positron",
    )

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

    terminal = nodes[nodes.index.isin(terminal_nodes)]

    catchment_map = terminal.explore(
        m=junction_map,
        color="yellow",
        marker_kwds={"radius": 10},
        tooltip=["osmid", "street_count"],
        popup=False,
    )

    catchment_map.save(f"./locations/test{filename}.html")


if __name__ == "__main__":
    # # scale free
    # print("==============================================")
    # print("==============================================")
    # print("==============================================")
    # print("SANJOSE")
    # display_central("sanjose", (14.5995, 120.9842), distance=2000, amenities=amenities)
    # print("==============================================")
    # print("==============================================")
    # print("==============================================")
    # print("ANGAT")
    # display_central(
    #     "angat",
    #     (14.953317761153066, 121.01155559567096),
    #     distance=2000,
    #     amenities=amenities,
    # )
    # print("==============================================")
    # print("==============================================")
    # print("==============================================")
    # print("SANRAFAEL")
    # display_central(
    #     "sanrafael",
    #     (14.99783531391446, 120.93040529499642),
    #     distance=2000,
    #     amenities=amenities,
    # )
    # print("==============================================")
    # print("==============================================")
    # print("==============================================")
    #
    # # grid
    # print("==============================================")
    # print("==============================================")
    # print("==============================================")
    # print("TONDO")
    # display_central("Tondo", "Tondo, Manila", amenities)
    display_central("Sampaloc", "Sampaloc, Manila", amenities)
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("QUIAPO")
# display_central("quiapo", "Quiapo, Manila", amenities)
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("ROTONDA")
# display_central("rotonda", (14.6197, 121.0053), distance=2000, amenities=amenities)
# print("==============================================")
# print("==============================================")
# print("==============================================")

# ring
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("qcmc")
# display_central("qcmc", (14.6514, 121.0497), distance=2000, amenities=amenities)
# display_central(
#    "pandi",
#    (14.875681235504679, 120.91910898845774),
#    distance=2000,
#    amenities=amenities,
# )
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("ulingao")
# display_central(
#    "ulingao",
#    (14.984113296438625, 120.90632193749528),
#    distance=2000,
#    amenities=amenities,
# )
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("==============================================")
# print("Kasibu")
# display_central(
#    "Kasibu, Nueva Vizcaya",
#    (16.27746639609076, 121.25314524596845),
#    distance=10000,
#    amenities=amenities,
# )
