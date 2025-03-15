import networkx as nx
import time


def get_subgraph(graph, nodes, landmarks):
    subgraphs = {}
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
            # print(service[0])
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
        subraph = graph.subgraph(catchment_area).copy()
        subgraphs[landmark["name"]] = subraph


def get_subgraph_benchmark(graph, nodes, landmarks):
    start_time = time.time()
    get_subgraph(graph, nodes, landmarks)
    runtime = time.time() - start_time
    return runtime


if __name__ == "__main__":
    print("get_Subgraph")
