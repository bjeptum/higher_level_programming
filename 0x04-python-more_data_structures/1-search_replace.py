#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return map(lambda search: search if search is not None else replace, my_list)
