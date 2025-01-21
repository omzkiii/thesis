def select_subgraph(nodes, landmarks):
    poi_geometries = landmarks["geometry"]
    service_nodes = nodes[
        nodes["geometry"].apply(
            lambda node: any(
                node.distance(poi) <= 0.0004 for poi in poi_geometries
            )  # 0.004 degrees approx 400 meters
        )
    ]

    catchment_nodes = nodes[
        nodes["geometry"].apply(
            lambda node: any(
                0.004 <= node.distance(poi) > 0.0005 for poi in poi_geometries
            )  # 0.004 degrees approx 400 meters
        )
    ]

    return service_nodes, catchment_nodes


if __name__ == "__main__":
    print("selecting subgraph")
