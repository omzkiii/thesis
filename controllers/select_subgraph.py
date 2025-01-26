import networkx as nx


def select_subgraph(graph, nodes, landmarks):
    subgraphs = {}
    origin_nodes = {}
    dest_nodes = {}
    for _, landmark in landmarks.iterrows():
        service_nodes = []
        catchment_area = []
        landmark_nodes = []
        dist = 0.0004
        while nodes[landmark_nodes].empty:
            landmark_nodes = nodes["geometry"].apply(
                lambda node: dist >= node.distance(landmark["geometry"]) >= 0
            )
            dist = dist + 0.0001
        for service in nodes[landmark_nodes].iterrows():
            service_nodes.append(service[0])
            for node in graph.nodes:
                try:
                    catchment = nx.shortest_path_length(
                        graph, source=node, target=service[0], weight="length"
                    )
                    if catchment <= 400:
                        catchment_area.append(node)
                except Exception as e:
                    pass
        origin_nodes[landmark["name"]] = service_nodes
        dest_nodes[landmark["name"]] = [
            node for node in catchment_area if node not in service_nodes
        ]
        subraph = graph.subgraph(catchment_area).copy()
        subgraphs[landmark["name"]] = (service_nodes, subraph)
    return subgraphs, origin_nodes, dest_nodes


if __name__ == "__main__":
    print("selecting subgraph")
