#chap4_43p_why max m

# Prim's algorithm with detailed logging for edge selection, cost updates, and decreasekey calls

import heapq

def prim_with_logging(graph, start_node):
    mst = []  # List to store the Minimum Spanning Tree edges
    total_cost = 0  # Total cost of the MST
    visited = set()  # Set to track visited nodes
    min_heap = [(0, start_node, None)]  # Priority queue (min-heap) with (cost, node, parent)
    
    decreasekey_count = 0  # Counter for decreasekey operations
    edge_scan_count = 0  # Counter for edges scanned
    
    cost_map = {node: float('inf') for node in graph}  # Store the minimum cost to reach each node
    cost_map[start_node] = 0  # Start node has 0 cost
    
    # Log initialization
    logs = []

    while min_heap:
        cost, node, parent = heapq.heappop(min_heap)
        
        if node not in visited:
            visited.add(node)
            if parent:
                mst.append((parent, node, cost))  # Add edge to the MST
                logs.append(f"Selected edge ({parent}, {node}) with cost {cost}")
            total_cost += cost
            
            # For each neighbor of the current node
            for neighbor, weight in graph[node]:
                edge_scan_count += 1  # Each edge is scanned here
                logs.append(f"Scanned edge ({node}, {neighbor}) with weight {weight}")
                
                # Only call decreasekey if this edge offers a cheaper path to neighbor
                if neighbor not in visited and cost_map[neighbor] > weight:
                    logs.append(f"cost({neighbor}) updated from {cost_map[neighbor]} to {weight}")
                    cost_map[neighbor] = weight  # Update with the lower cost
                    heapq.heappush(min_heap, (weight, neighbor, node))
                    decreasekey_count += 1  # decreasekey happens when the cost is updated
                    logs.append(f"Called decreasekey for ({neighbor}), new cost: {cost_map[neighbor]}")
            
            # Add a blank line after each vertex exploration to improve separation
            logs.append("")

    return mst, total_cost, edge_scan_count, decreasekey_count, logs

# Define the graph where decreasekey is not called for every edge
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('C', 3)],
    'C': [('A', 2), ('B', 3), ('D', 4)],
    'D': [('C', 4), ('E', 5)],
    'E': [('D', 5)]
}

# Run the algorithm with detailed logging
mst, total_cost, edge_scan_count, decreasekey_count, logs = prim_with_logging(graph, 'A')

# Output the results
for log in logs:
    print(log)

print("\nMST:", mst)
print("Total cost of the MST:", total_cost)
print("Total edges scanned:", edge_scan_count)
print("Total decreasekey calls:", decreasekey_count)
