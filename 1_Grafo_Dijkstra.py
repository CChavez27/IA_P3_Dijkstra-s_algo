import networkx as nx
import matplotlib.pyplot as plt

def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)
    if not di:
        G.add_edge(v, u, weight=w)

def dijkstra(G, start, end):
    # Obtener el camino más corto y su longitud utilizando Dijkstra
    path = nx.dijkstra_path(G, source=start, target=end)
    length = nx.dijkstra_path_length(G, source=start, target=end)
    return path, length

if __name__ == '__main__':
    G = nx.DiGraph()

    # Añadimos las aristas al grafo
    agregar_arista(G, "A", "B", 10)
    agregar_arista(G, "A", "D", 3)
    agregar_arista(G, "A", "E", 2)
    agregar_arista(G, "B", "C", 34, False)
    agregar_arista(G, "B", "E")
    agregar_arista(G, "C", "D", 3, False)
    agregar_arista(G, "C", "F", 1)
    agregar_arista(G, "D", "E", 2)
    agregar_arista(G, "D", "F", 10)
    agregar_arista(G, "E", "F", 8)

    # Ejecutar Dijkstra
    start_node = "A"
    end_node = "F"
    path, length = dijkstra(G, start_node, end_node)

    print(f"Camino más corto desde {start_node} hasta {end_node}: {path} con longitud {length}")

    # Dibujar el grafo
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Resaltar el camino más corto
    edge_colors = ['blue' if (u, v) in zip(path, path[1:]) else 'black' for u, v in G.edges()]
    node_colors = ['red' if n in path else 'white' for n in G.nodes()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)

    plt.title("Grafo con NetworkX - Camino más corto con Dijkstra")
    plt.show()
