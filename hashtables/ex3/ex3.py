def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    pairs = {}
    for array in arrays:
        for item in array:
            if item in pairs:
                pairs[item] += 1 
            else:
                pairs[item] = 1
                
    for i in pairs:
        if pairs[i] == len(arrays):
            result.append(i)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
