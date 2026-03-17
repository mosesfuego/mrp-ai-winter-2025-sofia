from src.perception.environment_analyzer import analyze_environment
from src.agent.planner_selector import choose_planner
from src.agent.tool_caller import call_tool

def run_agent(graph, start, goal):
    env_features = analyze_environment(len(graph), len(graph), 0.2, start, goal)
    planner_name = choose_planner(env_features)
    path = call_tool(planner_name, graph, start, goal)
    return path, planner_name
