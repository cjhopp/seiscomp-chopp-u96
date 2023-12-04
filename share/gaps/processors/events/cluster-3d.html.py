#!/usr/bin/python3

############################################################################
# Copyright (C) gempa GmbH                                                 #
#                                                                          #
# All Rights Reserved.                                                     #
#                                                                          #
# NOTICE: All information contained herein is, and remains                 #
# the property of gempa GmbH and its suppliers, if any. The intellectual   #
# and technical concepts contained herein are proprietary to gempa GmbH    #
# and its suppliers.                                                       #
# Dissemination of this information or reproduction of this material       #
# is strictly forbidden unless prior written permission is obtained        #
# from gempa GmbH.                                                         #
############################################################################


# The script generates a 3d plot based on the selected earthquakes using
# plotly (https://plotly.com). It performs a cluster search using DBSCAN
# (https://en.wikipedia.org/wiki/DBSCAN). The DBSCAN parameters
# "min_samples" and "eps" are defined by the number of selected
# earthquakes and the 90-percentile of the inter earthquake distances. The
# event markers are colored based on the cluster association.
#
# To install the required packages the following command should be
# executed on the GAPS system
#
# pip3 install --user scikit-learn plotly pandas


import sys
import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors


def process(source):
    try:
        catalog = pd.read_csv(source, header=1, sep=";")
        catalog.dropna(inplace=True, subset=("lat", "lon", "depth in km", "mag"))
    except Exception as e:
        raise ValueError(f"Could not read input: {e}") from e

    if catalog.empty:
        raise ValueError("Read empty catalog")

    # convert depth in similar dimension as coordinates
    catalog["scaledDepth"] = catalog["depth in km"] / 111.195079734632

    catalog.rename(
        columns={
            "lat": "Latitude",
            "lon": "Longitude",
            "depth in km": "Depth",
            "mag": "Magnitude",
            "region": "Region",
            "OT": "Time",
        },
        inplace=True,
    )
    x = catalog.loc[:, ["Latitude", "Longitude", "scaledDepth"]]

    # Try to derive best threshold for eps
    neigh = NearestNeighbors(n_neighbors=2)
    nbrs = neigh.fit(x)
    distances, _indices = nbrs.kneighbors(x)
    distances = np.sort(distances, axis=0)
    distances = distances[:, 1]
    idx = int(0.9 * (len(distances) - 1))
    threshold = distances[idx]
    minSample = max(int(np.log10(len(distances))), 5)

    # Cluster search based on DBSCAN
    dbscan = DBSCAN(eps=threshold, min_samples=minSample).fit(x)
    catalog["cluster"] = pd.Series(dbscan.labels_).astype("string")
    catalog.sort_values(by=["cluster"], inplace=True)
    catalog["cluster"].where(catalog["cluster"] != "-1", "outliers", inplace=True)
    catalog["cluster"] = catalog["cluster"].astype("category")
    catalog["scaledMag"] = np.exp(catalog["Magnitude"])
    catalog["scaledMag"].where(catalog["scaledMag"] >= 1, 1, inplace=True)

    # Define custom color scheme
    colorSequence = [
        "grey",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "teal",
        "magenta",
        "lime",
        "purple",
        "olive",
        "gold",
        "brown",
        "peru",
        "darkgreen",
        "aqua",
        "indigo",
        "pink",
    ]

    fig = px.scatter_3d(
        catalog,
        x="Longitude",
        y="Latitude",
        z="Depth",
        color="cluster",
        color_discrete_sequence=colorSequence,
        size="scaledMag",
        size_max=50,
        hover_data={
            "scaledMag": False,
            "scaledDepth": False,
            "eventID": True,
            "Time": True,
            "Magnitude": True,
        },
    )
    fig.update_scenes(zaxis_autorange="reversed")
    fig.write_html(sys.stdout)


def main():
    if len(sys.argv) <= 1 or sys.argv[1] == "-":
        source = sys.stdin
        sourcename = "standard input"
    else:
        source = sourcename = sys.argv[1]

    try:
        process(source)
    except Exception as e:
        print(f"Could not process '{sourcename}': {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
