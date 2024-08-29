from graph import Graph


# Example Map() function
def map_visit(node):
    print(f"{node}", end=" ")


# Example Fold() function to sum numeric values
def fold_sum(acc, node):
    if isinstance(node, (int, float)):
        return acc + node
    return acc


# Example Fold() function to how many nodes got visited
def fold_count(acc, node):
    return acc + 1


# Not-Oriented Graph Example
g = Graph()

g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode("A")

g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, "A")

# [START DEVELOPER TEST]

g.show()  # PRINT GRAPH STRUCTURE

print("\n--- MAP DFS:")
g.Dfs(map_func=map_visit)  # PERFORM DFS USING MAP

print("\n\n--- FOLD DFS:")
result = g.Dfs(fold_func=fold_sum, acc=0)  # PERFORM DFS USING FOLD
print(f"\t--- RESULT VALUE: {result}")

print("\n--- FOLD BFS STARTING FROM '1':")
node_count = g.Bfs(1, fold_func=fold_count, acc=0)  # PERFORM BFS USING FOLD
print(f"\t--- NUMBER OF VISITED NODES: {node_count}")

# [END DEVELOPER TEST]

# TODO: 1. ADD ENCAPSULATION
# TODO: 2. CYCLIC TEST
# TODO: 3. MINIMUM PATHS
# TODO: 4. TOPOLOGICAL SORT
# TODO: 5. SCC
# TODO: 6. ADD GRAPHICS
# TODO: 7. COMPLETE ONE ASD EXAM EXERCISE