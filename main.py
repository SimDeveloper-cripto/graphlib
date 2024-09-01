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

    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")

    g.addEdge("A", "B")
    g.addEdge("A", "C")
    g.addEdge("B", "D")
    g.addEdge("C", "D")
    g.addEdge("D", "E")

    # [START]

    # g.show()     # PRINT GRAPH STRUCTURE
    g.visualize()  # VISUALIZE THE GRAPH


'''
    print("\n--- MAP DFS:")
    g.Dfs(map_func=map_visit)  # PERFORM DFS USING MAP

    print("\n--- FOLD DFS:")
    result = g.Dfs(fold_func=fold_sum, acc=0)  # PERFORM DFS USING FOLD
    print(f"\t--- EMPTY MAP RESULT: {result}")

    print("\n--- MAP BFS STARTING FROM 'A':")
    g.Bfs("A", map_func=map_visit)  # PERFORM BFS USING MAP

    print("\n--- FOLD BFS STARTING FROM 'A':")
    node_count = g.Bfs("A", fold_func=fold_count, acc=0)  # PERFORM BFS USING FOLD
    print(f"\t--- NUMBER OF VISITED NODES: {node_count}")

    min_path = g.getMinimumPath("A", "E")
    print("\nMINIMUM PATH BETWEEN A & E:", min_path)
'''

    # [END]


if __name__ == "__main__":
    run_dev_test()

# TODO: 1. TOPOLOGICAL SORT
# TODO: 2. SCC
# TODO: 3. COMPLETE ONE ASD EXAM EXERCISE