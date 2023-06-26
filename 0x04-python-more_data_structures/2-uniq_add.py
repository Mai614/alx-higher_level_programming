#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    sum = 0
    for i in my_list:
        if i not in unique_set:
            sum += i
            unique_set.add(i)
    return sum
