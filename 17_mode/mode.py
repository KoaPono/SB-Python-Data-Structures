def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Create dictionary of number count
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num] = num_count.get(num) + 1
        else:
            num_count.update({num: 1})
    
    # Compare values to get largest value
    largest_value = 0
    largest_key = None
    for key in num_count.keys():
        if num_count[key] > largest_value:
            largest_value = num_count[key]
            largest_key = key
    return largest_key