from enum import Enum


# EACH GRAPH'S VERTEX HAS A COLOR
class Color(Enum):
    WHITE = 0  # Vertex Unvisited
    GRAY  = 1  # Vertex Explored but not Visited
    BLACK = 2  # Vertex Visited