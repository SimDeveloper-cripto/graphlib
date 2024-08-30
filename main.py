from graph import Graph


# Example Map() function to print visited nodes
def map_visit(node):
    print(f"{node}", end=" ")


# Example Fold() function to sum numeric values
def fold_sum(acc, node):
    if isinstance(node, (int, float)):
        return acc + node
    return acc


# Example Fold() function to count how many nodes got visited
def fold_count(acc, node):
    return acc + 1


def run_dev_test():
    g = Graph()

    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode("A")

    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, "A")

    # [START]

    g.show()  # PRINT GRAPH STRUCTURE

    print("\n--- MAP DFS:")
    g.Dfs(map_func=map_visit)  # PERFORM DFS USING MAP

    print("\n--- FOLD DFS:")
    result = g.Dfs(fold_func=fold_sum, acc=0)  # PERFORM DFS USING FOLD
    print(f"\t--- EMPTY MAP RESULT: {result}")

    print("\n--- MAP BFS STARTING FROM '1':")
    g.Bfs(1, map_func=map_visit)  # PERFORM BFS USING MAP

    print("\n--- FOLD BFS STARTING FROM '1':")
    node_count = g.Bfs(1, fold_func=fold_count, acc=0)  # PERFORM BFS USING FOLD
    print(f"\t--- NUMBER OF VISITED NODES: {node_count}")

    # [END]


if __name__ == "__main__":
    run_dev_test()

# TODO: 1. CYCLIC TEST
# TODO: 2. MINIMUM PATHS
# TODO: 3. TOPOLOGICAL SORT
# TODO: 4. SCC
# TODO: 5. ADD GRAPHICS
# TODO: 6. COMPLETE ONE ASD EXAM EXERCISE