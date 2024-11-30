from graphlib import UndirectedGraph
from graphlib.color import Color

# TODO: COMPLETE TEST SUITE #2, #3

# Test Map() function to print visited nodes
def __map_visit(node):
    print(f"{node}", end=" ")


# Test Fold() function to sum numeric values
def __fold_sum(acc, node):
    if isinstance(node, (int, float)):
        return acc + node
    return acc


# Test Fold() function to count how many nodes got visited
def __fold_count(acc, node):
    return acc + 1


def run_dev_test():
    g = UndirectedGraph()

    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")
    g.addNode("F")

    g.addEdge("A", "B", 1.0)
    g.addEdge("A", "C", 2.0)
    g.addEdge("B", "C", 2.5)
    g.addEdge("D", "E", 1.5)

    # [TEST #0 START]
    nodes = g.getNodes()
    if len(nodes) != 6:
        print("[TEST #0] GET_NODES: FAILED")
    print("[TEST #0] GET_NODES: PASSED")
    # [TEST #0 END]

    # [TEST #1 START]
    color = g.getNodeColor("A")
    # By accessing a 'random' vertex to check Its color, we can be sure of the correct implementation of:
    #   - addNode(node)
    #   - addEdge(node1, node2)
    if color != Color.WHITE:
        print("[TEST #1] GET_NODE_COLOR: FAILED")
    print("[TEST #1] GET_NODE_COLOR: PASSED")
    # [TEST #1 END]

    # [TEST #2 START]
    # Dfs with Map() & Fold()
    # [TEST #2 END]

    # [TEST #3 START]
    # Bfs with Map() & Fold()
    # [TEST #3 END]

    # [TEST #4 START]
    passed = False
    minimumPath = g.getMinimumPath("A", "C")
    if len(minimumPath) == 2:
        passed = True

    minimumPath = g.getMinimumPath("A", "F")
    if minimumPath is not None:
        passed = False

    if passed:
        print("[TEST #4] GET_MINIMUM_PATH: PASSED")
    else:
        print("[TEST #4] GET_MINIMUM_PATH: FAILED")
    # [TEST #4 END]

    # [TEST #5 START]
    sccs = g.getSCCs()
    if len(sccs) != 3:
        print("[TEST #5] GET_SCCS: FAILED")
    print("[TEST #5] GET_SCCS: PASSED")
    # [TEST #5 END]

    # [TEST #6 START]
    g.show()
    print("[TEST #6] SHOW_GRAPH_STATUS: PASSED")
    # [TEST #6 END]