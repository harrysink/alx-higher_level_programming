#!/usr/bin/python3
def best_score(a_dictionary):
    best = []
    if not a_dictionary:
        return None
    else:
        best = max(a_dictionary)
    return best
