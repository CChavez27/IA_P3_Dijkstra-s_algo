import networkx as nx
import matplotlib.pyplot as plt

def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)
    if not di:
        G.add_edge(v, u, weight=w)

def kruskal_mst(G):
    mst = nx.Graph()
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    subtrees = {node: {node} for node in G.nodes()}

    for u, v, data in edges:
        if subtrees[u] != subtrees[v]:
            mst.add_edge(u, v, weight=data['weight'])
            union = subtrees[u] | subtrees[v]
            for node in union:
                subtrees[node] = union

    return mst

if __name__ == '__main__':
    G = nx.Graph()

    agregar_arista(G, "A", "B", 50)
    agregar_arista(G, "A", "D", 41)
    agregar_arista(G, "A", "E", 22)
    agregar_arista(G, "B", "C", 13)
    agregar_arista(G, "B", "E", 44)
    agregar_arista(G, "C", "D", 35)
    agregar_arista(G, "C", "F", 56)
    agregar_arista(G, "D", "E", 37)
    agregar_arista(G, "D", "F", 48)
    agregar_arista(G, "E", "F", 89)

    # Dibujar el grafo original y el MST en subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Grafo original
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, ax=ax1, node_color='lightblue', with_labels=True, node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)
    ax1.set_title("Grafo Original")

    # MST usando Kruskal
    mst = kruskal_mst(G)
    pos_mst = nx.spring_layout(mst)
    nx.draw_networkx(mst, pos_mst, ax=ax2, node_color='lightgreen', with_labels=True, node_size=500)
    labels_mst = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos_mst, edge_labels=labels_mst, ax=ax2)
    ax2.set_title("Árbol de Expansión Mínima (MST) usando Kruskal")

    plt.tight_layout()
    plt.show()
