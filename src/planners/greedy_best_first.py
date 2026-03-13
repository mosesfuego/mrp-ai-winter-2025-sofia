import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def plan(graph, start, goal):
    """
    Greedy Best First Search
    """

    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {}
    visited = set()

    while frontier:

        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        visited.add(current)

        for neighbor in graph.neighbors(current):

            if neighbor in visited:
                continue

            priority = heuristic(neighbor, goal)

            heapq.heappush(frontier, (priority, neighbor))
            came_from[neighbor] = current

    if goal not in came_from:
        return None

    # reconstruct path
    node = goal
    path = [node]

    while node != start:
        node = came_from[node]
        path.append(node)

    path.reverse()

    return path
