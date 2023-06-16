def min_max_normalization(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = []
    for value in data:
        normalized_value = (value - min_val) / (max_val - min_val)
        normalized_data.append(normalized_value)
    return normalized_data