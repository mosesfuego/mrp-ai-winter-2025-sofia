import networkx as nx
import random


def create_grid(width, height):
    return nx.grid_2d_graph(width, height)


def add_obstacles(graph, width, height, density, start, goal):

    total_cells = width * height
    obstacle_count = int(total_cells * density)

    nodes = list(graph.nodes)

    # never place obstacle on start or goal
    nodes.remove(start)
    nodes.remove(goal)

    obstacles = random.sample(nodes, obstacle_count)

    for node in obstacles:
        if node in graph:
            graph.remove_node(node)

    return graph
