#!/usr/bin/python3
def best_score(a_dictionary):
    v = list(a_dictionary.values())
    k = list(a_dictionary.keys())
    best = k[v.index(max(v))]
    if best == 0:
        return None
    else:
        return best
