# When the ring buffer is FULL and a new element is inserted
# the OLDEST element is overwritten with the NEWEST element

#  two methods, append() and get()

# append
#   adds the given element to the buffer

# get 
#   returns all of the elements in a LIST, in their given order. 
#   Should NOT return any None values in the list even if present

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0 # starter & initial oldest element
        self.storage = [] # empty List, ?

    #adds the given element to the buffer
    def append(self, item):
        

    def get(self):
        pass