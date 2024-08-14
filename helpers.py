
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
        first = 1
    last = len(words)-1
    PositionOfNext = last - 1
    while PositionOfNext >= first:
        Next = words[PositionOfNext]
        current = PositionOfNext
        while current < last and Next > words[current + 1]:
            #sort them
            current += 1
            words[current - 1] = words[current]
        words[current] = Next
        #put somehting somewhere
        PositionOfNext -= 1
        #shorten the unsorted part
    pass

