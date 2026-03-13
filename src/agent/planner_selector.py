import random


def choose_planner(env):

    size = env["grid_size"]
    density = env["density"]

    if size < 150:
        return "bfs"

    if density < 0.12:
        return "greedy"

    if density > 0.35:
        return "dijkstra"

    return "astar"
