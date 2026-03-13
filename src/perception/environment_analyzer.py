def analyze_environment(width, height, obstacle_density, start, goal):

    grid_size = width * height

    start_goal_distance = abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    return {
        "grid_size": grid_size,
        "width": width,
        "height": height,
        "density": obstacle_density,
        "start_goal_distance": start_goal_distance,
    }
