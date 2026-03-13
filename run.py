from src.visualization.grid_visualizer import visualize
import random
from src.visualization.grid_visualizer import visualize
from src.environment.grid_world import create_grid, add_obstacles
from src.perception.environment_analyzer import analyze_environment
from src.agent.planner_selector import choose_planner
from src.agent.agent import run_agent


WIDTH = random.choice([10, 15, 20, 30])
HEIGHT = WIDTH

DENSITY = random.uniform(0.05, 0.4)

START = (0, 0)
GOAL = (WIDTH - 1, HEIGHT - 1)


def main():

    print("\n--- Creating Environment ---")

    graph = create_grid(WIDTH, HEIGHT)
    graph = add_obstacles(graph, WIDTH, HEIGHT, DENSITY, START, GOAL)
    env = analyze_environment(WIDTH, HEIGHT, DENSITY, START, GOAL)

    print("\n--- Environment Analysis ---")

    for key, value in env.items():
        print(f"{key}: {value}")

    planner = choose_planner(env)

    print("\n--- Planner Selected ---")
    print(planner)

    path = run_agent(graph, START, GOAL, planner)

    if path:

        print("\n--- Path Found ---")
        print("Path length:", len(path))
        print("Path:", path)
        visualize(graph, WIDTH, HEIGHT, path, START, GOAL)
        

    else:

        print("\nNo path found")


if __name__ == "__main__":
    main()
