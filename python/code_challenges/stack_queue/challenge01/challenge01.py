# Write here the code challenge solution

class Node:
    def __init__(self,value ):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    '''
    method append to put the node in the top of stack
    '''
    def append(self,value):
        node = Node(value)
        if self.top:
            node.next=self.top
        self.top=node
        self.size +=1

    ''' 
    pop method to delete the top node in the stack and return the the value of it
    '''
    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    '''
    peek methode to get the value of top node in stack 
    '''
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("Empty")
    '''
        get_size method to return the size of stack
    '''
    def get_size(self):
        return self.size

class Queue:

    def __init__(self) :
        self.Stack1=Stack()
        self.satck2=Stack()
        
    def enQueue(self, x):
        self.Stack1.append(x)
        

    def de_queue(self):   
        while self.Stack1.get_size():
                self.satck2.append(self.Stack1.pop()) 
        return self.satck2.pop()


    def peek(self):
        while self.Stack1.get_size():
                self.satck2.append(self.Stack1.pop()) 
        return self.satck2.peek()

    def empty(self):
        if self.Stack1.top ==None:
            return False
        else:
            return True
            
if __name__=="__main__":
    queue1=Queue()
    
    
    
    for i in range(6):
        queue1.enQueue(i)
    
    # print("peek value->>",queue1.peek())

    # for i in range(5):
    #     print(queue1.de_queue())

    print(queue1.empty())
    
   
    
    

    
    