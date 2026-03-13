from src.planners import bfs, astar, dijkstra, greedy_best_first


def run_agent(graph, start, goal, planner_name):

    planners = {
        "bfs": bfs.plan,
        "astar": astar.plan,
        "dijkstra": dijkstra.plan,
        "greedy": greedy_best_first.plan,
    }

    planner = planners[planner_name]

    path = planner(graph, start, goal)

    return path
