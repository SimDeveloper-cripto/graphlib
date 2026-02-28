import platform
import networkx as nx
import matplotlib.pyplot as plt

import multiprocessing
from .color import Color


def __visualize(graph, path=None, edges=None):
    system = platform.system()

    # USING NETWORKX API
    g = nx.Graph()

    node_list = graph.getNodes()
    for node in node_list:
        g.add_node(node)

    for i in range(len(node_list)):
        for j in range(i + 1, len(node_list)):
            connected, weight = graph.getMatrix()[i][j]
            if connected == 1:
                g.add_edge(node_list[i], node_list[j], weight=weight)

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
    node_colors = [color_map[graph.getCurrentStateOfColors()[node]] for node in node_list]
    font_colors = [b_f_color_map[graph.getCurrentStateOfColors()[node]] for node in node_list]

    edge_colors = []
    edges_to_highlight = set()
    nodes_to_highlight = set()

    if path:
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            edges_to_highlight.add((u, v))
            edges_to_highlight.add((v, u))
        nodes_to_highlight.update(path)

    if edges:
        for edge in edges:
            u, v = edge[0], edge[1]
            edges_to_highlight.add((u, v))
            edges_to_highlight.add((v, u))
            nodes_to_highlight.add(u)
            nodes_to_highlight.add(v)

    if nodes_to_highlight:
        for i, node in enumerate(node_list):
            if node in nodes_to_highlight:
                node_colors[i] = '#ff7f0e'  # Orange highlight
                font_colors[i] = 'white'

    for u, v in g.edges():
        if (u, v) in edges_to_highlight or (v, u) in edges_to_highlight:
            edge_colors.append('#d62728')  # Red highlight for edges
        else:
            edge_colors.append('gray')

    # DRAW USING __Matplotlib__
    pos = nx.circular_layout(g, scale=0.05)
    fig, ax = plt.subplots()

    fig.set_size_inches(8, 6)
    fig.canvas.manager.set_window_title('Graph Visualizer')

    nx.draw(
        g,
        pos,
        with_labels = True,
        node_color  = node_colors,
        edge_color  = edge_colors,
        width       = [2.0 if c == '#d62728' else 1.0 for c in edge_colors],
        node_size   = 1000,
        font_size   = 10,
        font_weight = 'bold',
        edgecolors  = font_colors
    )

    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    for node, (x, y) in pos.items():
        ax.text(
            x, y,
            s          = node,
            bbox       = dict(facecolor=node_colors[node_list.index(node)], edgecolor=font_colors[node_list.index(node)], boxstyle='round,pad=0.3'),
            color      = b_f_color_map[graph.getCurrentStateOfColors()[node]],
            fontsize   = 15,
            fontweight = 'bold',
            ha         = 'center',
            va         = 'center'
        )

    if system == "Linux":
        plt.savefig("output.png")
        print("[INFO] output.png has been generated!")
    else:
        plt.tight_layout()
        plt.show()

def visualizeState(graph, path=None, edges=None):
    process = multiprocessing.Process(target=__visualize, args=(graph, path, edges))
    process.start()