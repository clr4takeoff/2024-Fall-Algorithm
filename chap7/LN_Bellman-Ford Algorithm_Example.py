def staged_bellman_ford_precise(graph, vertices, source):
    # Initialize distances
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    # Organize graph as adjacency list for outgoing edges
    adjacency_list = {v: [] for v in vertices}
    for u, v, weight in graph:
        adjacency_list[u].append((v, weight))

    # Display initial state
    print("Stage 0:")
    print_table(dist, vertices)
    print("=" * 50)

    # Keep track of reachable vertices
    reachable = {source}

    # Perform staged relaxations
    for i in range(1, len(vertices)):
        updated = False
        next_reachable = set()
        print(f"Stage {i}:")

        iteration_log = []

        # Only process outgoing edges from currently reachable vertices
        for u in reachable:
            for v, weight in adjacency_list[u]:
                if dist[u] + weight < dist[v]:
                    old_dist = dist[v]
                    dist[v] = dist[u] + weight
                    updated = True
                    next_reachable.add(v)
                    iteration_log.append(
                        f"Updated dist[{v}] from {old_dist} to {dist[v]} using edge ({u} -> {v})"
                    )

        # Display updates in this stage
        if iteration_log:
            print("Changes in this stage:")
            for log in iteration_log:
                print(log)
        else:
            print("No changes in this stage.")

        # Update reachable vertices for the next stage
        reachable = reachable.union(next_reachable)

        # Display distances after this stage
        print_table(dist, vertices)
        print("=" * 50)

        # Exit early if no updates
        if not updated:
            print("No updates in this stage. Early exit.")
            break

    # Final distances
    print("Final distances after all stages:")
    print_table(dist, vertices)

# Helper function to print distances in a neatly aligned table format
def print_table(dist, vertices):
    header = " | ".join(f"{v:>3}" for v in vertices)
    values = " | ".join(f"{dist[v]:>3}" if dist[v] != float('inf') else "  ∞" for v in vertices)
    print(header)
    print(values)

# Define the graph as edge list (u, v, weight)
edges = [
    ('S', 'A', 10),
    ('S', 'G', 8),
    ('A', 'E', 2),
    ('B', 'C', 1),
    ('B', 'A', 1),
    ('C', 'D', 3),
    ('D', 'E', -1),
    ('E', 'B', -2),
    ('F', 'A', -4),
    ('F', 'E', -1),
    ('G', 'F', 1)
]

# Define vertices
vertices = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

# Run the staged Bellman-Ford algorithm
staged_bellman_ford_precise(edges, vertices, 'S')
