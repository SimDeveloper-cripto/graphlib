from graph import Graph

# Example Map() function
def visit(node):
    print(f"{node}", end=" ")

# Oriented Graph Example
# g = Graph(oriented=True) # It must be spelled 'oriented'

# Not-Oriented Graph Example
g = Graph(oriented=False) # It must be spelled 'oriented'

g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")

g.addEdge("A", "B")
g.addEdge("B", "C")

# [START TEST]

# ...

# [END TEST]

# TODO: CONTINUE IMPLEMENTATION OF graph.py
# TODO: PREPARE TEST FOR graph.py