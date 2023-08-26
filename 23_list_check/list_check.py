def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    return len([list_item for list_item in lst if isinstance(list_item, list)]) == len(lst)