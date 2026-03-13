import networkx as nx


def manhattan(a, b):
    """
    Manhattan distance heuristic.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def plan(graph, start, goal):
    """
    A* search path planning.
    """

    try:
        path = nx.astar_path(graph, start, goal, heuristic=manhattan)
        return path

    except nx.NetworkXNoPath:
        return None
