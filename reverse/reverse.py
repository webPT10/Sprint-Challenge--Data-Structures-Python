class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node == None:
            return None

        nextNode = node.get_next()
        if nextNode:
            node.set_next(prev)
            prev = node
            node = prev.get_next()

        if nextNode is None:
            self.head = node
            node.set_next(prev)
            return

        self.reverse_list(nextNode, prev)

        # count = 0
        # rooster = self.head

        # while rooster is not None: # while self.head is not None:

        #     self.add_to_head(rooster.value) # using add_to_head() method, pass in the self.HEAD.VALUE

        #     rooster = rooster.get_next() # call get_next() method, assigned to h, ?

        #     if count == 0:

        #         self.head.set_next(None) # ? on self.HEAD, apply set_next() method but set it to None as count == 0 ?

        #         count += 1
