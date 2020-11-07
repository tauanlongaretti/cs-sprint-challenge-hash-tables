def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    data = {}
        
    for item in range(length):
        data[weights[item]] = item

    for item in range(length):
        if limit - weights[item] in data:
            return (max(item, data[limit - weights[item]]), min(item, data[limit - weights[item]]))
            
    return None
