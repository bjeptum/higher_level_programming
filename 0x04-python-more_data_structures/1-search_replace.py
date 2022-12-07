#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            my_list.replace(i, replace)
            print(my_list)
