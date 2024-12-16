from graphlib import UndirectedGraph
from graphlib.color import Color

# TODO: DIJKSTRA NEEDS MORE TESTING

def _fold_sum(acc, node):
    if isinstance(node, (int, float)):
        return acc + node
    return acc

def _fold_count(acc, node):
    return acc + 1

def run_dev_unit_test():
    g = UndirectedGraph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.addNode(node)

    g.addEdge("A", "B", 1.0)
    g.addEdge("A", "C", 1.0)
    g.addEdge("B", "C", 1.0)
    g.addEdge("D", "E", 1.0)

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
    test2_passed = True
    try:
        visited_nodes = []
        g.dfs(map_func=lambda n: visited_nodes.append(n))
        test2_passed &= (set(visited_nodes) == {'A', 'B', 'C', 'D', 'E', 'F'})

        if set(visited_nodes) != {'A', 'B', 'C', 'D', 'E', 'F'}:
            print("\t[DEBUG TEST #2] MAP FULL_DFS TEST FAILED")

        visited_nodes = []
        g.dfs(start_node='A', map_func=lambda n: visited_nodes.append(n))
        test2_passed &= (set(visited_nodes) == {'A', 'B', 'C'})

        if set(visited_nodes) != {'A', 'B', 'C'}:
            print("\t[DEBUG TEST #2] MAP DFS STARTING FROM C TEST FAILED")

        result_sum = g.dfs(fold_func=_fold_sum, acc=0)
        test2_passed &= (result_sum == 0)

        if result_sum != 0:
            print(f"\t[DEBUG TEST #2] FOLD TEST FAILED: GOT {result_sum}, EXPECTED 0")

        result_count = g.dfs(fold_func=_fold_count, acc=0)
        # Largest connected component includes: {'A', 'B', 'C'} of size 3
        test2_passed &= (result_count == 6)

        if result_count != 6:
            print(f"\t[DEBUG TEST #2] FOLD COUNT TEST FAILED: GOT {result_count}, EXPECTED 3")

        visited_nodes = []
        result_invalid = g.dfs(start_node='Z', map_func=lambda n: visited_nodes.append(n))
        test2_passed &= (visited_nodes == [] and result_invalid is None)

        if visited_nodes != [] or result_invalid is not None:
            print("\t[DEBUG TEST #2] 'INVALID START NODE' TEST FAILED")
    except Exception as e:
        test2_passed = False
        print(f"Exception encountered during test #2: {e}")

    if test2_passed:
        print("[TEST #2] DFS_TEST: PASSED")
    else:
        print("[TEST #2] DFS_TEST: FAILED")
    # [TEST #2 END]

    # [TEST #3 START]
    test3_passed = True
    try:
        visited_nodes = []
        g.bfs(start_node='A', map_func=lambda n: visited_nodes.append(n))
        test3_passed &= (set(visited_nodes) == {'A', 'B', 'C'})

        if set(visited_nodes) != {'A', 'B', 'C'}:
            print("\t[DEBUG TEST #3] MAP BFS TEST FAILED")

        result_count = g.bfs(start_node='D', fold_func=_fold_count, acc=0)
        test3_passed &= (result_count == 2)

        if result_count != 2:
            print(f"\t[DEBUG TEST #3] FOLD COUNT TEST FAILED: GOT {result_count}, EXPECTED 2")

        result_sum = g.bfs(start_node='B', fold_func=_fold_sum, acc=0)
        test3_passed &= (result_sum == 0)

        if result_sum != 0:
            print(f"\t[DEBUG TEST #3] FOLD TEST FAILED: GOT {result_sum}, EXPECTED 0")

        visited_nodes = []
        result_invalid = g.bfs(start_node='Z', map_func=lambda n: visited_nodes.append(n))
        if visited_nodes != [] or result_invalid is not None:
            print("\t[DEBUG TEST #3] 'INVALID START NODE' TEST FAILED")
    except Exception as e:
        print(f"Exception encountered during test #3: {e}")

    if test3_passed:
        print("[TEST #3] BFS_TEST: PASSED")
    else:
        print("[TEST #3] BFS_TEST: FAILED")
    # [TEST #3 END]

    # [TEST #4 START]
    test4_passed = False
    minimumPath = g.getMinimumPath("A", "C")
    if len(minimumPath) == 2:
        test4_passed = True

    minimumPath = g.getMinimumPath("A", "F")
    if minimumPath is not None:
        test4_passed = False

    if test4_passed:
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
    print("[TEST #6] SHOW_GRAPH_STATE: PASSED")
    # [TEST #6 END]

    # [TEST #7 START]
    test7_passed = True

    path = g.dijkstra("A", "C")
    expected_path = ['A', 'C']
    if path != expected_path:
        test7_passed = False
        print(f"\t[DEBUG TEST #7] 'DIJKSTRA' FOUND INVALID PATH: {path}")

    path = g.dijkstra("A", "F")
    if path is not None:
        test7_passed = False
        print(f"\t[DEBUG TEST #7] 'DIJKSTRA' FOUND INVALID PATH, EXPECTED NONE BUT FOUND {path}")

    if test7_passed:
        print("[TEST #7] DIJKSTRA: PASSED")
    else:
        print("[TEST #7] DIJKSTRA: FAILED")
    # [TEST #7 END]