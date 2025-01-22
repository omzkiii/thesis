import geopandas as gpd


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

    subgraphs = {}
    for _, landmark in landmarks.iterrows():
        catchment = nodes["geometry"].apply(
            lambda node: 0.004 <= node.distance(landmark["geometry"]) > 0.0004
        )

        service = nodes["geometry"].apply(
            lambda node: 0.0004 <= node.distance(landmark["geometry"]) >= 0
        )
        landmark_gdf = gpd.GeoDataFrame(
            landmark.to_frame().T, geometry="geometry", crs=landmarks.crs
        )
        subgraphs[landmark["name"]] = (nodes[catchment], nodes[service], landmark_gdf)

    return subgraphs


if __name__ == "__main__":
    print("selecting subgraph")
