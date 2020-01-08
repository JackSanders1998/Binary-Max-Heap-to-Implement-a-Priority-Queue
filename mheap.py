"""
Jack Sanders
CIS 313
Lab 3
11/25/2019

Use a binary Max-Heap to implement a Priority Queue.
Most, if not all, my methods are based on the textbook - some more loosely than others.
"""


class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap

    def increase_key(self, data):   # helper method for insert (from textbook)
        i = self.length - 1         # will be using i for in this method because insert at index 0 for length 1 and index 1 for length 2 etc...
        if data < self.heap[i]:
            print("new data is smaller than current key")
        self.heap[i] = data         # insert data at self.length - 1
        while (i > 0) and (self.heap[self.__get_parent(i)] < self.heap[i]):
            self.__swap(self.__get_parent(i), i)        # swap with parent until the parent is larger or the root is reached
            i = self.__get_parent(i)                    # change i value

    def insert(self, data):     # from textbook
        """Insert an element into the heap.
        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root

        if self.length == self.max_size:    # check if heap is already full
            raise(IndexError)               # If full, raise error

        self.heap[self.length] = -1         # create a placeholder for where the data should be inserted
        self.length += 1                    # incrememnt length
        self.increase_key(data)             # call helper method above

    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]                 # first value in heap (root)

    def extract_max(self):      # from textbook
        """Remove and return the maximum value in the heap.
        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap

        if self.length == 0:                        # extracting from an empty heap
            raise KeyError                          # error
        max = self.heap[0]                          # max = first value in heap
        self.heap[0] = self.heap[self.length - 1]   # change root value to last value in heap
        self.length = self.length - 1               # decrement length
        self.__heapify(0)                           # call helper function __heapify with current index being new first value in heap
        return max

    def __heapify(self, curr_index, list_length = None):        # from textbook
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book

        l = self.__get_left(curr_index)
        r = self.__get_right(curr_index)
        if l < self.length and self.heap[l] > self.heap[curr_index]:
            largest = l             # largest is left is left index is bigger than current index
        else:
            largest = curr_index    # else, largest is current index
        if r < self.length and self.heap[r] > self.heap[largest]:
            largest = r             # largest is right if right index is bigger than current index
        if largest != curr_index:
            self.__swap(curr_index, largest)    # call swap if changes need to be made to current index
            self.__heapify(largest)             # recursive call

    def build_heap(self):       # from textbook
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book

        for i in range(self.length // 2 - 1, -1, -1):   # loops through all non-leaf nodes of the tree
            self.__heapify(i)       # call helper method

    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

def heap_sort(l):
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure

    temp = []           # heap value in inverse order
    result = []         # return value
    heap = max_heap(len(l), l)  # initalize heap
    heap.build_heap()           # build the heap

    for i in range(len(l)):             # loop through values in heap
        temp.append(heap.extract_max()) # append maximum values in the heap to temp list
                                        # temp list will be in inverse order
    for j in range(len(l)):             # loop through temp
        result.append(temp.pop())       # append popped value of temp to result (return list)
    return result