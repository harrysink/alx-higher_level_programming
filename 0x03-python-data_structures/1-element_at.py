#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(len(my_list)):
        if idx < 0:
            print("None")
        elif idx > len(my_list) - 1:
            print("None")
        else:
            return my_list[idx]
