
""" Complete each of the sorts! """

def bubble_sort(words):
    for n in range(len(words)-1,0,-1):
        swapped = False
        for i in range(n):
            if words[i] > words[i+1]:
                swapped = True
                words[i], words[i+1] = words[i+1], words[i]
                if not swapped:
                    return




def selection_sort(words):
    '''Write your code here!'''
    pass

def insertion_sort(words):
    '''Write your code here!'''
    pass

