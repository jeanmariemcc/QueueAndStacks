# NODE IMPLEMENTATION
# DO NOT MODIFY

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return self.data.__str__()

    def __repr__(self):
        return self.data.__repr__()
    
def main():
	  new_node = Node("first node data")
	  head = Node("second node data", new_node)
	  print(head.get_data())
    
    
main()
