from  generate_grid_network import create_grid_network
from assign_fidelities_to_the_edges import assign_fidelity_to_edges
from calculate_purification_rounds2 import calculate_purification_rounds
from assign_EDP import assign_entanglement_distribution_probabilities
from assing_ESP_to_nodes import assign_swapping_probabilities
import networkx as nx
from Calculate_ESP_for_PATH import calculate_esp_for_path
from generate_Requests6 import generate_requests
from assign_filtered_capacities import assign_filtered_capacities
from sort_requests import sort_requests
from get_all_edge_disjoint_paths import get_all_edge_disjoint_paths
from sort_paths_by_intermediate_nodes import sort_paths_by_intermediate_nodes
from assign_capacity_from_values import assign_capacity_from_values
from calculate_usable_capacity_for_path import calculate_usable_capacity_for_path
from calculate_required_threshold import calculate_required_threshold
import random
from compute_required_bell_pairs_2 import compute_required_bell_pairs
from calculate_windows import calculate_time_windows
from sort_requests_by_backup_window import sort_requests_by_backup_window



ESP_probability_range=(0.7,0.95)
EDP_Probability_range=(0.75, 1)
Num_of_nodes=2
Initial_Fidelty_range=(0.6, 0.9)
NUM_REQ=1
windows_time = 5
DEMAND_RANGE=(10, 10)
F_THRESHOLD_RANGE=(0.8, 0.9)
freq_for_capacity=100
CAPACITY_RANGE=(0,1000)
elemantary_entanglement_generation_rate=0.8
F_initial = random.uniform(0.6, 0.8)
lifetime_ratio_range=(0.1, 0.9)


G = create_grid_network(Num_of_nodes, draw=True)
G = assign_fidelity_to_edges(G, fidelity_range=Initial_Fidelty_range)
G = assign_entanglement_distribution_probabilities(G, prob_range=EDP_Probability_range)
G = assign_swapping_probabilities(G, prob_range=ESP_probability_range)

df_requests = generate_requests(
    num_requests=NUM_REQ,
    num_nodes=G.number_of_nodes(),
    demand_range=DEMAND_RANGE,
    f_threshold_range=F_THRESHOLD_RANGE,
    windows_time=windows_time,
    lifetime_ratio_range=lifetime_ratio_range
)

df_sorted = sort_requests(df_requests)
G = nx.convert_node_labels_to_integers(G)

# 2. Kapasiteleri atama
G = assign_filtered_capacities(
    G,
    freq_for_capacity=freq_for_capacity,
    CAPACITY_RANGE=CAPACITY_RANGE,
    elementary_entanglement_generation_rate=elemantary_entanglement_generation_rate
)

# 3. capacity değerlerini assign et
edge_values = {
    (u, v): G[u][v]['capacities']
    for u, v in G.edges()
    if 'capacities' in G[u][v]
}
G = assign_capacity_from_values(G, edge_values)

#print("\n--- Edge Kapasiteleri ---")
#for u, v in G.edges():
    #print(f"Edge ({u}, {v}): {G[u][v]['capacity']}")

# 4. Her request için path'leri ve usable capacity'yi hesapla

required_bell_pairs_list = []

for idx, request in df_sorted.iterrows():
    source = int(request['source'])
    destination = int(request['destination'])
    f_threshold = request['f_threshold']
    demand = request['demand']


    paths = get_all_edge_disjoint_paths(G, request)
    sorted_paths = sort_paths_by_intermediate_nodes(paths)

    windows_df = calculate_time_windows(df_requests)
    print(windows_df)


    #print(f"\nRequest {idx}: source={source}, dest={destination}, f_threshold={f_threshold}")
    
    for i, path in enumerate(sorted_paths):
        # float node varsa int'e çevir
        path = [int(node) for node in path]

        usable_cap = calculate_usable_capacity_for_path(G, path)
        required_thresh = calculate_required_threshold(f_threshold, path)

        


        rounds , F_final = calculate_purification_rounds(F_initial, required_thresh)
       
        # Bell pair hesapla (rounds None olsa bile kontrol ederek)
        if rounds is not None:
            bell_pairs = compute_required_bell_pairs(demand, rounds)
        else:
            bell_pairs = None




