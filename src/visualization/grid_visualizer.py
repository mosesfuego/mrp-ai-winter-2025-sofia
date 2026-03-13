import matplotlib.pyplot as plt
import time


def visualize(graph, width, height, path=None, start=None, goal=None):

    plt.figure(figsize=(6, 6))

    x = []
    y = []

    for node in graph.nodes:
        x.append(node[0])
        y.append(node[1])

    plt.scatter(x, y, c="lightgray")

    if start:
        plt.scatter(start[0], start[1], c="green", s=120, label="Start")

    if goal:
        plt.scatter(goal[0], goal[1], c="blue", s=120, label="Goal")

    if path:

        for step in path:

            plt.scatter(step[0], step[1], c="red", s=60)

            plt.pause(0.1)

    plt.title("Adaptive Grid Navigation Agent")

    plt.legend()

    plt.show()
