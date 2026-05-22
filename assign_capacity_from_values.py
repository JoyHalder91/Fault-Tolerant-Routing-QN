def assign_capacity_from_values(G, edge_values):
    for (u, v), value in edge_values.items():
        if isinstance(value, list):
            G[u][v]['capacity'] = len(value)  # Listeyse uzunluğunu ata
        else:
            G[u][v]['capacity'] = value  # Değilse direkt ata
    return G  # Mutlaka G'yi return et