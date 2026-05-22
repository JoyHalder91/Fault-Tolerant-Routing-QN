import random
import pandas as pd

def generate_requests(num_requests, num_nodes, demand_range, f_threshold_range):
    requests = []
    current_time = 0

    for _ in range(num_requests):
        source = random.randint(0, num_nodes - 1)
        destination = random.randint(0, num_nodes - 1)
        while destination == source:
            destination = random.randint(0, num_nodes - 1)

        # Zamanı Poisson dağılımı gibi artıralım
        current_time += random.expovariate(1.0 / (20 / num_requests))
        arrival_time = round(current_time, 2)
        leave_time = arrival_time + random.choice([2, 3])
        demand = random.randint(demand_range[0], demand_range[1])
        f_threshold=round(random.uniform(f_threshold_range[0], f_threshold_range[1]), 3)
        request = {
            'source': source,
            'destination': destination,
            'arrival_time': arrival_time,
            'leave_time': leave_time,
            'demand': demand,
            'f_threshold': f_threshold
        }

        requests.append(request)

    return pd.DataFrame(requests)
