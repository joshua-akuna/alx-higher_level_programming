#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0
    for val in my_list:
        total_score += (val[0] * val[1])
        total_weight += val[1]

    return (total_score / total_weight)
