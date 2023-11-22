class queue():
    def __init__(self):
        self.contents=[]
        self.element=None

    def isEmpty(self):
        if len(self.contents)==0:
            return True
        else:
            return False
    
    def push(self,elem):
        self.contents=self.contents+[elem]
        return 'element has been pushed\n'

    def pop(self):
        if self.isEmpty():
            return "queue is empty\n"
        else:
            self.element=self.contents[0]
            self.contents=[self.contents[i] for i in range(1,len(self.contents))]
            return f"{self.element} is the popped element\n"
    
    def peek(self):
        if self.isEmpty():
            return 'queue is empty\n'
        else:
            return f'{self.contents[0]} is in front of the queue\n'

choice=''   
queue_list=queue()
while choice !=4:
    choice=eval(input("Enter 1 to push to the queue:\nEnter 2 to pop from the queue\nEnter 3 to peek from the queue\nEnter 4 to exit from the queue\nInput---> "))

    if choice ==1 :
        elem=eval(input("Enter the element to be pushed to the queue: "))
        queue_list.push(elem)
        print("The element has been pushed to the queue")

    elif choice ==2:
        print(queue_list.pop())

    elif choice ==3:
        print(queue_list.peek())
        
    elif choice ==4:
        print("Exiting from the queue")
        break

    else:
        print("Invalid choice")
        continue