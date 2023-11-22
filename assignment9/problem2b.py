class stack():
    def __init__(self):
        self.contents=[]
        self.element=None

    def isEmpty(self):
        if len(self.contents)==0:
            return True
        else:
            return False

    def push(self,elem):
        self.contents+=[elem]
        return 'element has been pushed\n'

    def pop(self):
        
        if self.isEmpty():
            return 'stack is empty\n'
        else:
            self.element=self.contents[-1]
            self.contents=[self.contents[i] for i in range(0,len(self.contents)-1)]
            return f'{self.element} has been popped\n'
        
    def peek(self):
        if self.isEmpty():
            return 'stack is empty\n'
        else:
            return f'{self.contents[-1]} is at the top of the stack\n'
        
stack_list=stack()
choice=''
while choice!=4:
    choice=eval(input("Enter 1 to push to stack \nEnter 2 to pop from stack \nEnter 3 to peek from the stack \nEnter 4 to exit \nINPUT --->"))
    if choice == 1:
        element=eval(input('Enter the element to be pushed: '))
        print(stack_list.push(element))
        print(stack_list)
    elif choice ==2:
        print(stack_list.pop())

    elif choice ==3:
        print(stack_list.peek())

    elif choice ==4:
        print('Exiting from the stack')
        break

    else:
        print('Invalid choice')
        continue