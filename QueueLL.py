# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None 
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self):
        # JM
        # returns the data at the front of the queue, and `None` otherwise
        if self.is_empty():
            return None
        return self.front.get_data()


    def get_tail(self):
        # JM
        # returns the data at the tail of the queue, and `None` otherwise
        if self.is_empty():
            return None
        return self.tail.get_data()

    def deq(self):
        # FIXME
        # returns the data on the front of the queue and removes it, otherwise returns `None` if the queue is empty
        if self.is_empty():
            return None
        data = self.front.get_data()
        self.front = self.front.get_next()
        if self.is_empty():
            self.clear()
        return data

    def enq(self, data=None):
        # JM
        # adds a new `Node` with `data` to the tail of the queue
        new_node = Node(data)
        if self.tail != None:
            self.tail.set_next(new_node) # need to do this prior to reassigning self.tail to the new_node
        self.tail = new_node
        if self.front == None:
            self.front = new_node    
        return

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        # JM
        # returns `True` if the queue is empty, or `False` otherwise
        return self.front == None

    def clear(self):
        # JM
        # makes the queue empty
        self.front = None
        self.tail = None
        return


def main():
    s = QueueLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.enq(i)
    s.print()
    print("Is empty?", s.is_empty())
    print(f'get front: {s.get_front()}')
    print(f'get tail: {s.get_tail()}')
    #s.clear()
    #print("After clear, Is empty?", s.is_empty())
    #s.print()
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

