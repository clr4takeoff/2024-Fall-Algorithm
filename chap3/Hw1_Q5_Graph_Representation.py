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
pre_counter = 1
post_counter = 1
call_stack = []
edge_stack = []

# Function to perform DFS and track states
def dfs(v, parent=None):
    global pre_counter, post_counter
    # Set preorder and low value for the current node
    visited.add(v)
    preorder[v] = low[v] = pre_counter
    pre_counter += 1

    # Track the call in the call stack
    call_stack.append(v)
    print(f"Call Stack: {call_stack}")
    print(f"Exploring vertex: {v}, Parent: {parent}")
    
    for u in sorted(graph[v]):
        if u == parent:
            continue

        edge_stack.append((v, u))
        print(f"Edge Stack: {edge_stack}")

        if u not in visited:
            # Explore the edge (v, u)
            dfs(u, v)

            # Update low value of v after returning from u
            low[v] = min(low[v], low[u])

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
            low[v] = min(low[v], preorder[u])

        print(f"Updated low[{v}] to {low[v]} after exploring {u}")

    # Set postorder value after finishing all adjacent nodes
    postorder[v] = post_counter
    post_counter += 1

    # Pop the current call from the call stack
    call_stack.pop()
    print(f"Postorder[{v}] = {postorder[v]}")
    print(f"Call Stack after returning from vertex {v}: {call_stack}")
    print("-" * 50)

# Start DFS from vertex 5
dfs(5)

# Final output
print("Preorder values:", preorder)
print("Postorder values:", postorder)
print("Low values:", low)
