# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.push(item)

    def peek(self):
        # JM
        # returns the data on the top of the stack, and `None` otherwise
        if self.is_empty():
            return None
        return self.top.get_data()

    def pop(self):
        # JM
        # removes and returns the data on the top of the stack, otherwise returns `None` if the stack is empty
        if self.is_empty():
            return None
        data = self.top.get_data()
        self.top = self.top.get_next()
        return data

    def push(self, data=None):
        # adds a new `Node` with `data` on the top of the stack
        # JM
        if self.is_empty():
            self.top = Node(data)
        else:
            # otherwise create a top that points to the former top
            self.top = Node(data, self.top)
        return
        

    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")


    def is_empty(self):
        # JM
        # returns `True` if the stack is empty, or `False` otherwise
        return self.top == None

    def clear(self):
        # JM
        # makes the stack empty
        self.top = None
        return 

def main():
    # JM
    #l = list(range(1, 5))
    #s = StackLL(l)
    # end JM
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())

# Don't run main on import
if __name__ == "__main__":
    main()

