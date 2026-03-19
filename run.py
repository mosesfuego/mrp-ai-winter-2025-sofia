import random
from src.environment.grid_world import create_grid, add_obstacles
from src.agent.agent import run_agent
from src.visualization.grid_visualizer import visualize


def main():

    # ---------------------------
    # 1. Randomized Environment
    # ---------------------------
    WIDTH = random.choice([10, 15, 20, 25, 30])
    HEIGHT = WIDTH
    DENSITY = random.uniform(0.05, 0.4)

    START = (0, 0)
    GOAL = (WIDTH - 1, HEIGHT - 1)

    print("\n--- Creating Grid Environment ---")

    graph = create_grid(WIDTH, HEIGHT)
    graph = add_obstacles(graph, WIDTH, HEIGHT, DENSITY, START, GOAL)

    # ---------------------------
    # 2. Run Agent
    # ---------------------------
    path, planner_name = run_agent(graph, START, GOAL)

    # ---------------------------
    # 3. Output
    # ---------------------------
    print("\n--- Final Planner Used ---")
    print(planner_name)

    if path:
        print("\n--- Path Found ---")
        print("Path length:", len(path))
    else:
        print("\nNo path found.")

    # ---------------------------
    # 4. Visualization
    # ---------------------------
    all_nodes = set((x, y) for x in range(WIDTH) for y in range(HEIGHT))
    obstacles = list(all_nodes - set(graph.nodes))

    visualize(
        graph,
        WIDTH,
        HEIGHT,
        path,
        START,
        GOAL,
        obstacles=obstacles,
        delay=0.5
    )


if __name__ == "__main__":
    main()
