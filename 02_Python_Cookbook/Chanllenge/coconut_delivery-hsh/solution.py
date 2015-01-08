##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2015-01-01             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
Compatibility: compatible to python2, python3

Prerequisit: None
"""

from __future__ import print_function
from collections import OrderedDict
import pprint
import json
import sys

def load_data(fname): # read data from raw data file
    """
    returns
    -------
        regular_rate: constant
        all_path: [ [start, end, energy_consumption, saving_rate, total_saved] ]
    """
    with open(fname, "r") as f:
        line = f.readline() # read the first line
        regular_rate = int(line.strip())
        
        all_path = dict() # read the rest of lines
        index = 0
        for line in f.readlines():
            index += 1
            start, end, energy_consumption = [int(i) for i in line.strip().split(" ")]
            all_path[index] = [start, 
                               end, 
                               energy_consumption, 
                               regular_rate - energy_consumption * 1.0 /(end - start), 
                               regular_rate * (end - start) - energy_consumption]
    
    return regular_rate, all_path


def get_data_description(regular_rate, all_path): # print some data features
    """see comment
    """
    max_end = max([path[1] for path in all_path.values()]) # the destination distance
    num_of_path = len(all_path) # how many paths
    print("""We are looking for opt-path from 0 to %s, there's %s paths we can choose. 
    regular energy consumption per mile = %s.""" % (max_end, num_of_path, regular_rate))    
    return max_end, num_of_path


def sort_path_by_total_saved(all_path):
    all_path_sorted_by_total_saved = {k: v[4] for k, v in all_path.items()}    
    all_path_sorted_by_total_saved = OrderedDict( sorted(list(all_path_sorted_by_total_saved.items()), 
                                                         key=lambda t: t[1], # sorted by value
                                                         reverse = True) ) # descent
    return all_path_sorted_by_total_saved


def is_overlap( interval1, interval2 ):
    """interval = (start, end)
    return True, overlapped
    return False, non-overlapped
    
    example:
        (3, 5) - (5, 8) False
        (3, 5) - (2, 4) True
    """
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 <= start2:
        if end1 <= start2:
            return False
        else:
            return True
    elif start2 < start1 < end2:
        return True
    else:
        return False
    
def exam_if_we_can_use_this_path(test_path_index, used_path_index, all_path):
    """Given a path, and all the path we have used, see if we can use this one (not overlapped with
    any of path we have used).
    
    test_path_index:
        use all_path[index] we can get:
            [start, end, energy_consumption, saving_rate, total_saved]
    
    used_path_index: set of path index we use
        for index in used_path_index:
            print(all_path[index]) 
        
        we can get: [ path1, path2, ..., ], these are the paths info we already used
    """
    for index in used_path_index:
        if is_overlap( (all_path[index][0], all_path[index][1]), 
                       (all_path[test_path_index][0], all_path[test_path_index][1]) ): # if overlapped
            return False # we cannot use
    return True # pass all exam, so we can use


def display_result(used_path_index, all_path, regular_rate, max_end):
    """after we get all path we have used, we sort them by the start point, calculate
    total energy we used, save result into result.txt.
    """
    ## result = dict( {index: start} ), then we sort the result by start, so it's human readable  
    result = {index: all_path[index][0] for index in used_path_index}
    result = OrderedDict( sorted(list(result.items()), 
                                 key=lambda t: t[1], # sorted by value
                                 reverse = False) ) # ascend
    
    choosed_path = list() # save the actual path here (not the index)
    total_energy_consumption = regular_rate * max_end # if we don't use any jet stream
    for index in result:
        choosed_path.append(all_path[index])
        total_energy_consumption -= all_path[index][4] # minus the energy we saved

    with open("result.txt", "w") as f:
        f.write( pprint.pformat(choosed_path) )
        
    print("total energy consumption = %s" % total_energy_consumption)
    print("goto result.txt to browse result.")


def main():
    """Main function
    
    namespace
    ---------
    
        regular_rate: which is the constant energy it takes to fly 1 mile WITHOUT jet streams.
    
        all_path: 
            [1: path1, 
             2: path2, ...
             5000: path5000,]
         
            path = [start, end, energy_consumption, saving_rate, total_saved]
        
        max_end: we are looking for opt path from 0 - #max_end
        
        num_of_path: how many path we can use in raw data
        
        all_path_sorted_by_total_saved: a list of index of path sorted by total_saved.
            if we use path which index, then this path saves most.
            
        used_path_index: the path row number we have used
            
    """
    _FNAME = "sample_paths.txt" 
#     _FNAME = "flight_paths.txt"
    regular_rate, all_path = load_data(_FNAME) # load raw data, derive #saving_rate, #total_saved 
    max_end, num_of_path = get_data_description(regular_rate, all_path) # find the end point, num of path
    all_path_sorted_by_total_saved = sort_path_by_total_saved(all_path) # sort path by #total_saved
    
    used_path_index = list() # for saving memory, we only store index
    
    while 1:
        flag = 1 # every time we start looking for the next usable path, set flag = 1
        for index in all_path_sorted_by_total_saved:
            if exam_if_we_can_use_this_path(index, 
                                            used_path_index,
                                            all_path):
                used_path_index.append(index)
                
                # if we can find a path, we shut off the flag. if we cannot find any usable path
                # flag remains 1, then we can jump out the while loop
                flag = 0 
                break # if found one, jump out for loop
        del all_path_sorted_by_total_saved[index] # remove used path from sorted path index
        if flag: # exam flag
            break        
    
    display_result(used_path_index, all_path, regular_rate, max_end)

main()