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

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.element=self.contents[-1]
            self.contents=[self.contents[i] for i in range(0,len(self.contents)-1)]
            return self.element
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.contents[-1]
        
string=input('Enter the equation: ')
opening_bracket=['[','(','{']
closing_bracket=[']',')','}']

st=stack()

for i in string:
    if i in opening_bracket:
        st.push(i)
    elif i in closing_bracket:
        a=closing_bracket.index(i)
        e=st.peek()
        if opening_bracket[a] == e:
            st.pop()        
    
if st.isEmpty():
    print(1)
else:
    print(0)
    