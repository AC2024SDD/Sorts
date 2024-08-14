
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
    '''Write your code here!'''
    pass

