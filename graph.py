from color import Color
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


# NON-ORIENTED GRAPH IMPLEMENTED BY MATRIX
class Graph:
    def __init__(self):
        self.__nodes  = []       # List to hold nodes
        self.__matrix = []       # Adjacency Matrix
        self.__node_colors = {}  # Dictionary to track colors of nodes

    def __Init(self):
        for node in self.__node_colors:
            self.__node_colors[node] = Color.WHITE

    def __resize_matrix(self, new_size):
        old_size  = len(self.__matrix)
        curr_size = new_size - old_size

        # Expand existing rows
        for row in self.__matrix:
            row.extend([0] * curr_size)

        # Add new rows
        for _ in range(curr_size):
            self.__matrix.append([0] * new_size)

    def addNode(self, node):
        if node not in self.__nodes:
            self.__nodes.append(node)
            self.__resize_matrix(len(self.__nodes))
            self.__node_colors[node] = Color.WHITE

    def addEdge(self, node1, node2):
        if node1 not in self.__nodes:
            self.addNode(node1)
        if node2 not in self.__nodes:
            self.addNode(node2)

        index1 = self.__nodes.index(node1)
        index2 = self.__nodes.index(node2)
        self.__matrix[index1][index2] = 1
        self.__matrix[index2][index1] = 1

    def getNodes(self):
        return self.__nodes

    def getCurrentStateOfColors(self):
        return self.__node_colors

    def show(self):
        col_width = max(len(str(node)) for node in self.__nodes) + 2

        print(" " * (col_width + 1) + "|", end="")
        for node in self.__nodes:
            print(f" {str(node):<{col_width}}", end="")
        print()

        print(" " * (col_width + 1) + "+" + "-" * ((col_width + 1) * len(self.__nodes)))
        for i, row in enumerate(self.__matrix):
            print(f"{str(self.__nodes[i]):<{col_width}} |", end="")
            for val in row:
                print(f" {val:<{col_width}}", end="")
            print()

    def visualize(self):
        # USING NETWORKX API
        g = nx.Graph()

        for node in self.__nodes:
            g.add_node(node)

        for i in range(len(self.__nodes)):
            for j in range(len(self.__nodes)):
                if self.__matrix[i][j] == 1:
                    g.add_edge(self.__nodes[i], self.__nodes[j])

        color_map = {
            Color.WHITE: 'white',
            Color.GRAY:  'gray',
            Color.BLACK: 'black',
        }
        b_f_color_map = {
            Color.WHITE: 'black',
            Color.GRAY:  'black',
            Color.BLACK: 'white'
        }
        edge_color = 'gray'

        node_colors = [color_map[self.__node_colors[node]] for node in self.__nodes]
        font_colors = [b_f_color_map[self.__node_colors[node]] for node in self.__nodes]

        # DRAW USING __Matplotlib__
        pos = nx.spring_layout(g)
        fig, ax = plt.subplots()

        fig.canvas.manager.set_window_title('Graph Visualizer')

        nx.draw(
            g,
            pos,
            with_labels = True,
            node_color  = node_colors,
            edge_color  = edge_color,
            node_size   = 2000,
            font_size   = 15,
            font_weight = 'bold',
            edgecolors = font_colors
        )

        for node, (x, y) in pos.items():
            ax.text(
                x, y,
                s          = node,
                bbox       = dict(facecolor=node_colors[self.__nodes.index(node)], edgecolor=font_colors[self.__nodes.index(node)], boxstyle='round,pad=0.3'),
                color      = b_f_color_map[self.__node_colors[node]],
                fontsize   = 15,
                fontweight = 'bold',
                ha         = 'center',
                va         = 'center'
            )

        # ax.set_title("Graph Visualizer", fontsize=20, fontweight='bold')
        plt.show()

    def __DfsVisit(self, node, map_func=None, fold_func=None, acc=None):
        if map_func is not None:
            map_func(node)

        if fold_func is not None:
            acc = fold_func(acc, node)

        self.__node_colors[node] = Color.GRAY

        index = self.__nodes.index(node)
        for i, connected in enumerate(self.__matrix[index]):
            if connected and self.__node_colors[self.__nodes[i]] == Color.WHITE:
                acc = self.__DfsVisit(self.__nodes[i], map_func, fold_func, acc)

        self.__node_colors[node] = Color.BLACK
        return acc

    # DFS WITH BOTH MAP AND FOLD
    def Dfs(self, map_func=None, fold_func=None, acc=None):
        self.__Init()
        for node in self.__nodes:
            if self.__node_colors[node] == Color.WHITE:
                acc = self.__DfsVisit(node, map_func, fold_func, acc)

        return acc

    # BFS WITH BOTH MAP AND FOLD
    def Bfs(self, start_node, map_func=None, fold_func=None, acc=None):
        if start_node not in self.__nodes:
            return acc

        self.__Init()
        queue = [start_node]
        self.__node_colors[start_node] = Color.GRAY

        while queue:
            curr = queue.pop(0)
            if map_func is not None:
                map_func(curr)

            if fold_func is not None:
                acc = fold_func(acc, curr)

            index = self.__nodes.index(curr)
            for i, connected in enumerate(self.__matrix[index]):
                if connected and self.__node_colors[self.__nodes[i]] == Color.WHITE:
                    queue.append(self.__nodes[i])
                    self.__node_colors[self.__nodes[i]] = Color.GRAY

            self.__node_colors[curr] = Color.BLACK
        return acc

    # GET MINUMUM PATH BETWEEN TWO NODES
    def getMinimumPath(self, start_node, end_node):
        if start_node not in self.__nodes or end_node not in self.__nodes:
            return None

        self.__Init()
        queue = deque([(start_node, [start_node])])  # Tuple of (curr_node, path)
        self.__node_colors[start_node] = Color.GRAY

        while queue:
            curr, path = queue.popleft()
            if curr == end_node:
                return path

            index = self.__nodes.index(curr)
            for i, connected in enumerate(self.__matrix[index]):
                node_v = self.__nodes[i]
                if connected and self.__node_colors[node_v] == Color.WHITE:
                    self.__node_colors[node_v] = Color.GRAY
                    queue.append((node_v, path + [node_v]))

            self.__node_colors[curr] = Color.BLACK
        return None