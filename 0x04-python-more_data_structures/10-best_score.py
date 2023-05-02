#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    v = list(a_dictionary.values())
    k = list(a_dictionary.keys())

    if not v:
        return None
    best_score = max(v)
    if best_score in v:
        return k[v.index(best_score)]
    else:
        return None
