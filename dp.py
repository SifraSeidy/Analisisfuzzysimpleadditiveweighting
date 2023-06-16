def calculate_optimal_order(preferences, weights):
    n = len(preferences)
    table = [0] * (n+1)

    for i in range(1, n+1):
        table[i] = preferences[i-1] * weights[(i-1) % len(weights)] + table[i-1] * weights[i % len(weights)]

    optimal_order = [i for i in range(1, n+1) if table[i] == max(table)]
    return optimal_order

preferences = [0.7875, 0.875, 0.5875, 0.475, 0.5625, 0.775, 0.525, 0.4125, 0.8375, 0.6, 0.4625, 0.6625, 0.725, 0.6875, 0.525, 0.4125, 0.8375, 0.6, 0.675, 0.8375, 0.4125, 0.525, 0.65, 0.65, 0.9]
weights = [0.35, 0.25, 0.25, 0.15]

optimal_order = calculate_optimal_order(preferences, weights)
print("Urutan kenaikan jabatan yang optimal:", optimal_order)