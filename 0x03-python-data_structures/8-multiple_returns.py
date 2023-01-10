#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = (len(sentence), sentence[0])
    if len(sentence) == 0:
        my_tuple = (0, "None")
    return my_tuple
