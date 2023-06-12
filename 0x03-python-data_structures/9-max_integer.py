#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        biggest_int = my_list[0]
        for i in range(len(my_list)):
            if biggest_int < my_list[i]:
                biggest_int = my_list[i]
        return biggest_int 
