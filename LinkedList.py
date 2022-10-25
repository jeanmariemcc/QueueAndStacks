# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        # JM 
        #  returns the data in the head node, and `None` otherwise
        if self.is_empty():
            return None
        return self.head.get_data()

    def add(self, data):
        # JM - this is a pre-pend function
        # if a new LinkedList, create the head
        if self.is_empty():
            self.head = Node(data)
        else:
            # otherwise create a head that points to the former head
            self.head = Node(data, self.head)
        return

    def search(self, data):
        # JM
        # returns `True` if `data` is in the list, or `False` otherwise
        if self.is_empty():
            return False
        if self.head.get_data() == data:
            return True
        current = self.head
        while current.get_next() != None:
            if current.get_next().get_data() == data:
                return True
            current = current.get_next()
        return False


    def delete(self, data):
        # JM
        # searches for `data` in the list,
        # removes it if found and returns it, 
        # otherwise returns `None` and makes no change to the list
        if self.is_empty():
            return None
        if self.head.get_data() == data:
            # finding the data in the header is a special case - 
            # eliminate the header by making the next node the headere
            self.head = self.head.get_next()
            return data
        current = self.head
        while current.get_next() != None:
            # the header current node does not contain the data
            # so keep checking if there is a next node
            if current.get_next().get_data() == data:
                # if current node +1 has the data,
                # have the pointer in the current node point around it.
                # e.g. if found in 2, have 1 point to 3
                current.next_node = current.get_next().get_next()
                return data
            current = current.get_next()
        return None
        

    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")


    def is_empty(self):
        # JM
        return self.head == None

    def clear(self):
        # JM
        self.head = None
        return 

def main():
    l = list(range(1, 5))
    print(l)
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll.print()

# Don't run main on import
if __name__ == "__main__":
    main()

