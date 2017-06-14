def find_max_min(the_list):
    """
    returns the a list with values of the minimum and maximum number, 
    a list with the item length if bot min and max are equal
    """
    min_max = []
    min_num = min(the_list)
    max_num = max(the_list)
    all_equal = []

    if min_num == max_num:
        the_value = int(len(the_list))
        all_equal.append(the_value)
        return all_equal
    else:
        min_max.append(min_num)
        min_max.append(max_num)
        return min_max 



