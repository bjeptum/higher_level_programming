#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers
    tuple (<score>, <weight>)
    """
    if not my_list:
        return 0
    weighted_sum = 0
    weight_sum = 0
    for score, weight in my_list:
        weighted_sum += score * weight
        weight_sum += weight
    return (weighted_sum / weight_sum)
