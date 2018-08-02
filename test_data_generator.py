
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from numpy import random as random_generator
from time import time
import collections


# Generate several lists to be sorted and return a tuple
# data structure that will contain the following:
# an already sorted list, a sorted list in reverse and
# a randomly unsorted list of numbers. this will be used
# to test sorting algorithms for best, common and worst case
# scenarios !
def lists_generator(end_number: int, list_size: int) -> ([int], [int], [int]):
    already_sorted_list = list(range(list_size))
    random_sorted_list = random_generator.randint(end_number, size=list_size).tolist()
    reverse_sorted_list = already_sorted_list[::-1]
    return already_sorted_list, random_sorted_list, reverse_sorted_list


# takes a function that accepts array/list of integers.
# returns array/list of integers and a float representing
# the execution time of the function in milliseconds.
def time_it(function_to_time, function_input: [int]) -> ([int], float):
    start_time = float(time() * 1000)
    function_output = function_to_time(function_input)
    end_time = float(time() * 1000)
    return function_output, (end_time - start_time)


# takes two arrays/lists of integers and compare
# each element with the other. will return True
# if both arrays/lists are of same size and each
# element on same index equal to the other.
def compare_equal(list_one: [int], list_two: [int]) -> bool:

    if len(list_one) != len(list_two):
        return False

    lists_size: int = len(list_one)  # doesnt matter which size you get, they both are same size
    index: int = 0

    if lists_size == 1:
        return list_one[0] == list_two[0]

    while index < lists_size:
        if list_one[index] != list_two[index]:
            return False
        index = index + 1

    return True  # if we get here , then we existed the loop without returning False, elements equal each other


# makes a copy of list to sort, apply python's built in sort and return the copy sorted.
# wrote this, because the default sort behaviour will sort the actual list passed.
# we don't want that, so we can reuse the original list in other tests.
def sort(list_to_sort: [int]) -> [int]:

    if len(list_to_sort) <= 1:
        return list_to_sort

    sorted_list = list(list_to_sort)
    return sorted(sorted_list)


# used for pretty display of information on function behaviour and time complexity.
# by default it will generate time complexity info, unless visualization_on is set to True,
# then it will display how function algorithm behaves visually!
def analyze(title: str, func, in_list: [int], visualization_on: bool = False):
    print("-------------Testing {}-------------".format(title))
    if visualization_on:
        func(in_list, True)
    else:
        (result, time_ms) = time_it(func, in_list)
        print("In {} ms, list {} was sorted to {}".format(time_ms, in_list, result))
    print("-------------End of Testing {}-------------".format(title))
    print()  # creating a new line


# FIXME: get rid of the bellow if compare_equal works
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)