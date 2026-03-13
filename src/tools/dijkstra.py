import networkx as nx


def plan(graph, start, goal):
    """
    Dijkstra shortest path planning.
    """

    try:
        path = nx.dijkstra_path(graph, source=start, target=goal)
        return path

    except nx.NetworkXNoPath:
        return None
