# hw1 Question5

# Graph Representation based on the given graph (adjacency list)
graph = {
    1: [2, 3],
    2: [1, 3, 4, 5],
    3: [1, 2],
    4: [2, 5, 6],
    5: [2, 4, 6],
    6: [4, 5, 7, 8],
    7: [6, 8],
    8: [6, 7]
}

# Variables to track DFS state
preorder = {}
postorder = {}
low = {}
visited = set()
counter = 1
call_stack = []
edge_stack = []

# Function to perform DFS and track states
def dfs(v, parent=None):
    global counter
    # Set preorder and low value for the current node
    visited.add(v)
    preorder[v] = low[v] = counter
    print(f"Initial low[{v}] set to {low[v]} (preorder value = {preorder[v]})")
    counter += 1

    # Track the call in the call stack
    call_stack.append(v)
    print(f"Call Stack: {call_stack}")
    print(f"Exploring vertex: {v}, Parent: {parent}")

    for u in sorted(graph[v]):
        if u == parent:
            continue

        # Add edge to stack if it has not been added already
        if (v, u) not in edge_stack and (u, v) not in edge_stack:
            edge_stack.append((v, u))
            print(f"Edge Stack: {edge_stack}")

        if u not in visited:
            # Explore the edge (v, u)
            dfs(u, v)

            # Update low value of v after returning from u
            original_low_v = low[v]
            low[v] = min(low[v], low[u])
            print(f"Updated low[{v}] from {original_low_v} to {low[v]} after exploring child {u}")

            # Articulation point condition (not root)
            if low[u] >= preorder[v]:
                print(f"Articulation point found at vertex: {v}")
                component = []
                while edge_stack:
                    e = edge_stack.pop()
                    component.append(e)
                    if e == (v, u):
                        break
                print(f"Biconnected component: {component}")

        else:
            # Update the low value of v considering back edge (v, u)
            original_low_v = low[v]
            low[v] = min(low[v], preorder[u])
            print(f"Updated low[{v}] from {original_low_v} to {low[v]} due to back edge to {u}")

    # Set postorder value after finishing all adjacent nodes
    postorder[v] = counter
    print(f"Postorder[{v}] set to {postorder[v]}")
    counter += 1

    # Pop the current call from the call stack
    call_stack.pop()
    print(f"Call Stack after returning from vertex {v}: {call_stack}")
    print("-" * 50)

# Start DFS from vertex 5
dfs(5)

# After DFS finishes, if there are any edges left in edge_stack, they form a biconnected component.
if edge_stack:
    print("Remaining edges in edge_stack indicate a final biconnected component.")
    component = []
    while edge_stack:
        component.append(edge_stack.pop())
    print(f"Final Biconnected component: {component}")

# Final output
print("Preorder values:", preorder)
print("Postorder values:", postorder)
print("Low values:", low)

# Display the [preorder, postorder] pair for each node
print("Node traversal orders:")
for node in sorted(graph.keys()):
    if node in preorder and node in postorder:
        print(f"Node {node}: [Preorder = {preorder[node]}, Postorder = {postorder[node]}]")

