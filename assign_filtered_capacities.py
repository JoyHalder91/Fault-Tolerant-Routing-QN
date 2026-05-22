import networkx as nx
import random

def assign_filtered_capacities(G, freq_for_capacity, CAPACITY_RANGE, elementary_entanglement_generation_rate):
    max_capacity = CAPACITY_RANGE[1]
    capacity_threshold = max_capacity * elementary_entanglement_generation_rate

    for u, v in G.edges():
        capacity_values = [random.randint(CAPACITY_RANGE[0], CAPACITY_RANGE[1]) for _ in range(freq_for_capacity)]
        filtered_capacities = [val for val in capacity_values if val < capacity_threshold]
        G[u][v]['capacities'] = filtered_capacities  # Liste olarak sakla

    return G  # Mutlaka G'yi return et