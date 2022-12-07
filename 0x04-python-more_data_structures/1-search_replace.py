#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    for item in my_list:
        if item == search:
            my_list[count] = replace
            break
        count += 1
