import networkx as nx
import time


def select_subgraph(graph, nodes, landmarks):
    subgraphs = {}
    origin_nodes = {}
    dest_nodes = {}
    nodes = nodes.to_crs(epsg=3857)
    landmarks = landmarks.to_crs(epsg=3857)
    no_of_landmarks = 0
    for _, landmark in landmarks.iterrows():
        no_of_landmarks += 1
        print(landmark)
        service_nodes = []
        catchment_area = []
        landmark_nodes = []
        dist = 40
        while nodes[landmark_nodes].empty:
            landmark_nodes = nodes["geometry"].apply(
                lambda node: dist >= node.distance(landmark["geometry"]) >= 0
            )
            dist = dist + 10
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

        print(landmark)
        # print(nodes)
        origin_nodes = service_nodes
        dest_nodes = [node for node in catchment_area if node not in service_nodes]
        subraph = graph.subgraph(catchment_area).copy()
        sub_nodes = nodes[nodes.index.isin(catchment_area)]
        subgraphs[landmark["name"]] = (subraph, sub_nodes, landmark)

        print("========================")
        print(dest_nodes)
        print(origin_nodes)
        print(catchment_area)
        print("========================")
    print("========================")
    print("========================")
    print("========================")
    print(f"NUMBER OF LANDMARKS: {no_of_landmarks}")
    print("========================")
    print("========================")
    print("========================")
    return subgraphs


def select_subgraph_benchmark(graph, nodes, landmarks):
    start_time = time.time()
    select_subgraph(graph, nodes, landmarks)
    runtime = time.time() - start_time
    return runtime


if __name__ == "__main__":
    print("selecting subgraph")
