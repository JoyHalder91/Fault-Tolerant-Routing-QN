
import networkx as nx
import matplotlib.pyplot as plt

def create_grid_network(N, draw=True):
    """
    NxN boyutunda bir grid (ızgara) network oluşturur.
    
    Parametreler:
    - N (int): Grid boyutu (NxN)
    - draw (bool): True ise grafiği çizer.
    
    Dönüş:
    - G (networkx.Graph): Oluşturulan grid graph
    """
    # Grid graph oluştur
    G = nx.grid_2d_graph(N, N)

    # Görselleştirme için node pozisyonları
    pos = {(x, y): (y, -x) for x, y in G.nodes()}

    #if draw:
    #    plt.figure(figsize=(6, 6))
    #    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    #    plt.title(f"{N}x{N} Grid Network")
    #    plt.show()

    return G