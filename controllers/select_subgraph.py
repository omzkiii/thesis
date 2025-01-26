import networkx as nx


def select_subgraph(graph, nodes, landmarks):
    subgraphs = {}
    for _, landmark in landmarks.iterrows():
        service_nodes = []
        catchment_area = []
        landmark_nodes = nodes["geometry"].apply(
            lambda node: 0.0004 >= node.distance(landmark["geometry"]) >= 0
        )
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
        if len(service_nodes) != 0:
            subraph = graph.subgraph(catchment_area).copy()
            subgraphs[landmark["name"]] = (service_nodes, subraph)
    return subgraphs


if __name__ == "__main__":
    print("selecting subgraph")
