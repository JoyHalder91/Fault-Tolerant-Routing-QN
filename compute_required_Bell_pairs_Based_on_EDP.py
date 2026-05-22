import math

def compute_required_bell_pairs(G):
    """
    Her bir edge için, purification_rounds ve entanglement_prob değerlerine göre
    gereken Bell pair sayısını hesaplar ve 'required_bell_pairs' olarak ekler.
    """
    for u, v in G.edges():
        L = G[u][v].get('purification_rounds')
        p = G[u][v].get('entanglement_prob')

        if L is not None and p is not None and p > 0:
            required_bell_pairs = math.ceil(L / p)
            G[u][v]['required_bell_pairs'] = required_bell_pairs
        else:
            G[u][v]['required_bell_pairs'] = None  # Hesaplanamıyorsa None bırak

    return G