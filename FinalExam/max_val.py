def max_val(t):
    """
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    """
    def find_all_int(data):
        int_list = []
        for item in data:
            if isinstance(item, list) or isinstance(item, tuple):
                int_list.extend(find_all_int(item))
            elif isinstance(item, int):
                int_list.append(item)
        return int_list
    return max(find_all_int(t))


print(max_val((5, (1,2), [[1],[9]])))