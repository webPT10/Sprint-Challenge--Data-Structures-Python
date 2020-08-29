# When FULL and a new element is inserted
# OLDEST element is overwritten with the NEWEST element

# append()
#   adds the given element to the buffer

# get()
#   returns all of the elements in a LIST, in their given order. 
#   Should NOT return any None values in the list even if present

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0 # starter & initial oldest element
        self.storage = [] # empty List, ?

    #adds the given element to the buffer
    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.oldest] = item # assign item to [], ?
            self.oldest += 1 # increment oldest by 1

            if self.oldest > self.capacity-1:
                self.oldest = 0
        
        else:
            self.storage.append(item) # recurision, ?
        
    def get(self):
        return self.storage # returns the []/List which holds the elements