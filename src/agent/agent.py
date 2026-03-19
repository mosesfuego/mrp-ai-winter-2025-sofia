from src.perception.environment_analyzer import analyze_environment
from src.agent.planner_selector import choose_planner
from src.agent.tool_caller import call_tool
from src.agent.llm_planner import choose_planner_with_llm


def run_agent(graph, start, goal):

    # ---------------------------
    # 1. Perception
    # ---------------------------
    width = max(n[0] for n in graph.nodes) + 1
    height = max(n[1] for n in graph.nodes) + 1

    total_cells = width * height
    free_cells = len(graph.nodes)
    obstacle_density = 1 - (free_cells / total_cells)

    env_features = analyze_environment(
        width=width,
        height=height,
        obstacle_density=obstacle_density,
        start=start,
        goal=goal
    )

    print("\n--- Environment Features ---")
    for k, v in env_features.items():
        print(f"{k}: {v}")

    # ---------------------------
    # 2. LLM Decision
    # ---------------------------
    planner_name = choose_planner_with_llm(env_features)

    if planner_name:
        print("\n[LLM Selected Planner]:", planner_name)
    else:
        print("\n[LLM Failed → Using Fallback Rules]")
        planner_name = choose_planner(env_features)

    # ---------------------------
    # 3. Tool Execution
    # ---------------------------
    path = call_tool(planner_name, graph, start, goal)

    return path, planner_name
