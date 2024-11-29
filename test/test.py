from graphlib import UndirectedGraph

# TODO: IMPLEMENT A TEST SUITE

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

    # [TEST #0 START]
    # g.show()
    # print("\n[TEST #0] SHOW GRAPH STATUS: PASSED")
    # [TEST #0 END]

    # [TEST #1 START]
    sccs = g.getSCCs()
    if len(sccs) != 3:
        print("\n[TEST #1] GET_SCCS: FAILED")
    print("\n[TEST #1] GET_SCCS: PASSED")
    # [TEST #1 END]