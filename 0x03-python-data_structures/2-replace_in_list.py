#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    return [element if i == idx else i for i in my_list]
print(my_list)
