""" Your challenge is to implement a bubble sort, selection sort and insertion sort below. """

import helpers as h
import sorts as s
import csv
from time import perf_counter
path = (r"assets/words4000.csv")
#path = (r"assets/words10000.csv")
#path = (r"assets/words50000.csv")
word_list = []


def main():
    h.load_list(path)
    
    time = perf_counter()
    s.bubble_sort(word_list)
    print("Bubble sort completed in", perf_counter() - time)
    
    time = perf_counter()
    s.selection_sort(word_list)
    print("Selection sort completed in", perf_counter() - time)
    
    time = perf_counter()
    s.insertion_sort(word_list)
    print("Insertion sort completed in", perf_counter() - time)
    

if __name__ == "__main__":
    main()
