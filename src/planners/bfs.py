import networkx as nx


def plan(graph, start, goal):
    """
    Breadth First Search path planning.

    Parameters
    ----------
    graph : networkx.Graph
    start : tuple
    goal : tuple

    Returns
    -------
    path : list of nodes
    """

    try:
        path = nx.shortest_path(graph, source=start, target=goal)
        return path

    except nx.NetworkXNoPath:
        return None
