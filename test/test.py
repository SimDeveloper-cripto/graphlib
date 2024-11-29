from graphlib import UndirectedGraph

# TODO: COMPLETE TEST SUITE

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

    g.addEdge("A", "B")
    g.addEdge("A", "C")
    g.addEdge("B", "C")
    g.addEdge("D", "E")

    # [TEST #1 START]
    nodes = g.getNodes()
    if len(nodes) != 6:
        print("[TEST #1] GET_NODES: FAILED")
    print("[TEST #1] GET_NODES: PASSED")
    # [TEST #1 END]

    # [TEST #2 START]

    # [TEST #2 END]

    # [TEST #3 START]

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
    print("[TEST #6] SHOW GRAPH STATUS: PASSED")
    # [TEST #6 END]