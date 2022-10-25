# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Project 5: Implementing ADTs
#Given a stack defined by a `top` index and an `array`, please implement the following methods:

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    def peek(self):
        # JM
        # * `peek()`: returns the data on the top of the stack, and `None` otherwise 
        if self.is_empty():
            return None
        return self.array[self.top]

    def pop(self):
        # JM
        # * `pop()`: returns the data on the top of the stack, otherwise returns `None` if the stack is empty
        if self.is_empty():
            return None
        data = self.array[self.top]
        self.array[self.top] = 0
        self.top -= 1
        return data

    def push(self, data=None):
        # JM
        # * `push(data)`: puts `data` on the top of the stack
        if self.is_empty():
            self.array = [] # since we cannot modify the __init__, we need to clear the array prior to adding data
        # cannot use any built in functions, so concatenate two arrays
        temp_array = [data]
        self.array = self.array + temp_array
        self.top += 1
        return

    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        # JM
        # * `is_empty()`: returns `True` if the stack is empty, or `False` otherwise
        return self.top < 0

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
        # JM
        # * `clear():` makes the stack empty
        self.array = [0 for i in range(len(self.array))]
        self.top = -1
        return

    def size(self):
        return self.top + 1


def main():
    """
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    """
    s = StackArray(5)
    le = []
    la = []
    for i in range(20,201,10):
        s.push(i)
        le.insert(0,i)
    s.print()
    print(f'le: {le}')

    while not s.is_empty():
        la.append(s.pop())
    print(f'le: {le}')
    print(f'la: {la}')


# Don't run main on import
if __name__ == "__main__":
    main()

