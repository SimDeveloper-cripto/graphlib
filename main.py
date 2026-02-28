from graphlib.api import UndirectedGraph
from tests.unit_test import run_dev_unit_test

def run_user_test(g):
    path = g.dijkstra("A", "F")

    print(f"Shortest path from A to F: {path}")
    g.show(path=path)

def run_prim_test(g):
    mst_edges = g.prim("A")

    print(f"Archi del Minimum Spanning Tree (Prim): {mst_edges}")
    g.show(edges=mst_edges)

def run_kruskal_test(g):
    mst_edges = g.kruskal()

    print(f"Archi del Minimum Spanning Tree (Kruskal): {mst_edges}")
    g.show(edges=mst_edges)

if __name__ == "__main__":
    # run_dev_unit_test()  # it generates output.png + all unit tests

    g = UndirectedGraph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.addNode(node)

    g.addEdge("A", "B", 1.0)
    g.addEdge("A", "C", 2.0)
    g.addEdge("B", "C", 1.0)
    g.addEdge("C", "D", 1.0)
    g.addEdge("D", "E", 4.0)
    g.addEdge("C", "E", 2.0)
    g.addEdge("E", "F", 1.0)

    # run_user_test(g)
    # run_prim_test(g)
    run_kruskal_test(g)