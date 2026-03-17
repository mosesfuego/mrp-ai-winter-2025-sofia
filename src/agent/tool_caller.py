from src.tools import bfs, dijkstra, astar, greedy_best_first

TOOLS = {
    "bfs": bfs.plan,
    "dijkstra": dijkstra.plan,
    "astar": astar.plan,
    "greedy": greedy_best_first.plan,
}

def call_tool(tool_name, graph, start, goal):
    """
    Unified interface for agent to call any planner.
    """
    if tool_name not in TOOLS:
        raise ValueError(f"Unknown tool {tool_name}")
    return TOOLS[tool_name](graph, start, goal)
