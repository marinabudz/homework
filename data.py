class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
class LinkedList:
    def __init__(self, root = None): 
        self.root = root
        self.size = 0
    def add(self, data):
        new_node = Node(data,self.root)
        self.root = new_node
        self.size +=1
    def __repr__(self):
        next_n = self.root
        res = ''

        while next_n:
            res += str(next_n.data) + "->"
            next_n= next_n.next_node
        return res

my_list = LinkedList()
my_list.add(5)
my_list.add(9)
my_list.add(7)
# print(my_list)



class SLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "SLLNode object dat = {}".format(self.data) 

    def get_data(self):
        # "return the self.data attribuet"
        return self.data

    def set_data(self, new_data):
        # "replaced existing value of self.data with the new_data parameter"
        self.data = new_data
        
    def get_next(self):
        # "return the  self.next attribuet"
        return self.next


    def set_next(self, new_next):
        # "replaced existing value of self.next with the new_next parameter"
        self.next = new_next
# node = SLLNode('apple')
# print(node.get_data())
# node.set_data(8)
# print(node.get_data())
# node2 =SLLNode('carrot')
# node.set_next(node2)
# print(node.get_next())


class DLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    def __repr__(self):
        return "DLLNode object dat = {}".format(self.data) 

    def get_data(self):
        # "return the self.data attribuet"
        return self.data

    def set_data(self, new_data):
        # "replaced existing value of self.data with the new_data parameter"
        self.data = new_data
        
    def get_next(self):
        # "return the  self.next attribuet"
        return self.next

    def set_next(self, new_next):
        # "replaced existing value of self.next with the new_next parameter"
        self.next = new_next

    def get_previous(self):
        # "return the self.previous attribuet"
        return self.previous

    def set_previous(self, new_previous):
        # "replaced existing value of self.previous with the new_previous parameter"
        self.previous = new_previous



    
# node1= DLLNode(1)
# node2 = DLLNode(2)
# print(node1.get_previous())
# node1.set_previous(node2)
# print(node1.get_previous())


class SLL:
    def __init__(self):
        self.head = None
    def __repr__(self):
        return "SLL object head = {}".format(self.head)


    def is_empty(self):
        # return true is the linked list is empty and false if it isnt 
        return self.head is None

    def add_front(self, new_data):
        # create singly linked list Node whose data is a new_data argument to the front of the linked list (!!!! it is node object and NOT the string that conatins a word)
        temp = SLLNode(new_data)
        # when we created new node its default value will be equal to None /But we dont wanna it to be None so we reassing so self.head becomes equal to a n ew value instead of being equal to none
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        #  traverses (обходить) the linked list and return integer value representing the number of nodes in linked list
        # the time complexity is 0(n) because every node in the linked list must be visited in ordr to calculate the size of the linked list 
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None:
            size+=1
            current = current.get_next()
        return size

    def search(self, data):
        # traverses the linked list and return true if the data searched for is presented in one of the Nodes otherwise returns false  
        if self.head is None:
            return "linked list is empty. No nodes to search"
        current = self.head
        while current is not None:
            # the nodes data matches to what we are looking for
            if current.get_data() == data:
                return True 
            # it doesnt match
            else:
                current= current.get_next() 
        return False

    def remove(self, data):
        # removes the first occurence of the node that contains the data argument as its self.data variable .return nothing 
        if self.head == None:
            return 'nothing to remove.list is empty'
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return 'node with this value isnt presented  '
                else:
                    previous = current 
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



sll = SLL()
print(sll.size())
print(sll.is_empty())

sll.add_front('berry')
sll.add_front('cabbage')
sll.add_front('garlic')
print(sll.remove(15))

print(sll)
print(sll.size())
print(sll.remove('garlic'))
print(sll)
print(sll.size())
# print(sll.head)
# print(sll.size())
# print(sll.search('berry'))
class nodes:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    def __repr__(self):
        return 'Node object is {},  previous object is {} and next object is {}'.format(self.data,self.previous,self.next)
    def get_data(self):
        return self.data
    def set_data(self,new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def get_previous(self):
        return self.previous
    def set_previous(self, new_previous):
        self.previous = new_previous

# Create a double linked list class, i.e., a list where each element has an attribute previous and an attribute next,
#  and of course previous and next are also instances of the same class.   
class node:
    def __init__(self):
        self.head = None
    def __repr__(self):
        return 'Node object is{}'.format(self.head)
    
    def is_empty(self):
        # return true is the linked list is empty and false if it isnt 
        return self.head is None

    def add_front(self, new_data):
        # create singly linked list Node whose data is a new_data argument to the front of the linked list (!!!! it is node object and NOT the string that conatins a word)
        temp = DLLNode(new_data)
        # when we created new node its default value will be equal to None /But we dont wanna it to be None so we reassing so self.head becomes equal to a n ew value instead of being equal to none
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp

    def size(self):
        #  traverses (обходить) the linked list and return integer value representing the number of nodes in linked list
        # the time complexity is 0(n) because every node in the linked list must be visited in ordr to calculate the size of the linked list 
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None:
            size+=1
            current = current.get_next()
        return size

    def search(self, data):
        # traverses the linked list and return true if the data searched for is presented in one of the Nodes otherwise returns false  
        if self.head is None:
            return "linked list is empty. No nodes to search"
        current = self.head
        while current is not None:
            # the nodes data matches to what we are looking for
            if current.get_data() == data:
                return True 
            # it doesnt match
            else:
                current= current.get_next() 
        return False

    def remove(self, data):
        # removes the first occurence of the node that contains the data argument as its self.data variable .return nothing 
        if self.head == None:
            return 'nothing to remove.list is empty'
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return 'node with this value isnt presented  '
                else:
                    previous = current 
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    

node5 = node()
print(node5)
node5.add_front(10)
node5.head

print(node5)
# node5.set_previous('potato')
# print(node5)