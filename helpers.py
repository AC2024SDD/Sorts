
""" Complete each of the sorts! """

def bubble_sort(words):
    last = len(words)
    swapped = True
    while swapped == True:
        swapped = False
        i = 1
        while i < last:
            if words[i] > words[i+1]:
                temp = words[i]
                words[i] = words[i+1]
                words[i+1] = temp
                swapped = True
            i =+ 1
        last =- 1
    return words

def selection_sort(words):
    '''Write your code here!'''
    pass

def insertion_sort(words):
    for number in range(len(array)):
        current_number = number
        prev_num = current_number - 1
        while current_number > 0 and words[prev_num] > words[current_number]:
            words[current_number], words[prev_num] = words[prev_num], words[current_number]
            current_number += -1
            prev_num = current_number - 1

