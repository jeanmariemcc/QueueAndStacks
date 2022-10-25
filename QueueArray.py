# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 5: Queue-Array
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Technical HW: Implementing ADTs

class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)] # a fixed size array that acts as a circular queue by use of front and tail pointers, initialized to all zeroes
        self.front = -1  # index into self.array holding the front of the queue
        self.tail = -1  # index into self.array holding the last element of the queue

    def get_front(self):
        # JM
        # returns the data at the front of the queue, and `None` otherwise
        if self.is_empty():
            return None
        return self.array[self.front]

    def get_tail(self):
        # JM
        # returns the data at the tail of the queue, and `None` otherwise
        if self.is_empty():
            return None
        return self.array[self.tail]


    def deq(self):
        # JM
        # returns the data on the front of the queue and removes it, otherwise returns `None` if the queue is empty
        if self.is_empty():
            return None
        data = self.get_front()
        self.array[self.front] = 0
        self.front += 1
        if self.front  > self.tail:
            # if true, the deq has cleared the array,
            # reset the front and tail pointers
            self.tail = -1
            self.front = -1
        elif self.front > len(self.array):
            self.front = 0
        return data

    def enq(self, data=None):
        # JM
        # puts `data` on the tail of the circular queue
        if data == None:
            return None
        # if this is the first entry, initialize the front and clear the array (because I cannot modify __init__)
        if self.is_empty():
            self.front = 0
            self.array = []
       
        # the following code will accomodate a queue where #  A: front index is less than or equal to tail - 
        #      [front,.,.,.,.,tail] and [front tail]
        #   and
        #  B: front index is greater than tail (a circular queue had developed)
        #      [., ., ., tail, front, ., ., ]
        if self.is_full():
            array1 = self.array[self.front:]
            if len(array1) < len(self.array):
                array2 = self.array[0:self.tail]
            else:
                array2 = []
            temp_array = [data]
            self.array = array1 + temp_array + array2
            self.front = 0
            self.tail = len(self.array) -1
            return

        self.tail += 1
              
        if self.tail >= len(self.array) and not self.is_full(): # create a circular queue
            self.tail = 0
            
        self.array[self.tail] = data
        return


    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")


    def is_empty(self):
        # returns boolean True if empty
        # returns `True` if the queue is empty, or `False` otherwise
        return self.size() == 0

    def clear(self):
        # JM 
        # Empties the queue array
        # by inserting zeroes in all loctions
        # does not change the length of the queue array
        self.array = [0 for i in range(len(self.array))]
        self.front = -1
        self.tail = -1
        return

    def is_full(self):
        l = self.size()
        return l >= len(self.array)

    def size(self):
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l
    

def main():
    """
    
    s = QueueArray()
    s.print()
    print("Is empty?", s.is_empty())
    print(s.array)  # JM
    
    for i in range(1, 4):
        s.enq(i)
        print("Size:", s.size())
        s.print()
    s.print()
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    s.print()
    for i in range(5, 11):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    print("Front:", s.get_front())
    print("Tail: ", s.get_tail())
    print("Deq:  ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())
    print("Size:", s.size())
    """
    s = QueueArray()
    le = []
    la = []
    for i in range(20,201,10):
        s.enq(i)
        le.append(i)
    print(f'le 1st: {le}')
    s.print
    
    while not s.is_empty():
        la.append(s.deq())
    print(f'le: {le}')
    print(f'la: {la}')


# Don't run main on import
if __name__ == "__main__":
    main()

