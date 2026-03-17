import matplotlib.pyplot as plt

def visualize(graph, width, height, path=None, start=None, goal=None, obstacles=None, delay=0.5):
    """
    Animated visualization of the grid environment.

    Parameters:
    - graph: NetworkX grid graph (nodes without obstacles)
    - width, height: grid dimensions
    - path: list of (x, y) nodes
    - start, goal: coordinates
    - obstacles: list of obstacle coordinates
    - delay: seconds between animation frames
    """

    plt.figure(figsize=(7, 7))
    plt.xlim(-1, width)
    plt.ylim(-1, height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()  # (0,0) top-left

    # Draw free cells
    free_x = [n[0] for n in graph.nodes]
    free_y = [n[1] for n in graph.nodes]
    plt.scatter(free_x, free_y, c="lightgreen", marker='s', s=120, label="Free Space")

    # Draw obstacles
    if obstacles:
        ox = [o[0] for o in obstacles]
        oy = [o[1] for o in obstacles]
        plt.scatter(ox, oy, c="saddlebrown", marker='^', s=150, label="Obstacle (Tree/Mountain)")

    # Draw start and goal
    if start:
        plt.scatter(start[0], start[1], c="green", s=200, label="Start", marker='o')
    if goal:
        plt.scatter(goal[0], goal[1], c="blue", s=200, label="Goal", marker='*')

    plt.legend(loc="upper right")
    plt.title("Adaptive Grid Navigation Agent")
    plt.pause(0.5)  # pause before animation starts

    # Animate agent moving along the path
    if path:
        agent_plot, = plt.plot([], [], 'ro', markersize=15)

        for step in path:
            # Matplotlib requires sequences, not scalars
            agent_plot.set_data([step[0]], [step[1]])
            plt.pause(delay)

        # Ensure final position is shown
        agent_plot.set_data([path[-1][0]], [path[-1][1]])

    plt.show()
    plt.close()  # closes the current figure
