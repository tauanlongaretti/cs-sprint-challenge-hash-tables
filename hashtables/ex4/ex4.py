def has_negatives(a):
    """
    YOUR CODE HERE
    """
    pairs = {}
    result = []

    for num in a:
        if -num in pairs:
            result.append(abs(num))
        else:
             pairs[num] = 0

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
