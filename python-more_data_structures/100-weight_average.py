#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    total_weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight

    if total_weight == 0:  # Check if the total weight is zero to avoid division by zero
        return 0

    return total_weighted_score / total_weight
