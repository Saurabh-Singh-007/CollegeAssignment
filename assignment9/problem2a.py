class ic152():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    def check(self):
        if self.marks <33:
            return 'Fail'
        else:
            return 'Pass'

try:  
    marks=int(input('Enter the marks: '))
    name=input('Enter the name: ')
    roll_no=input('Enter the roll number: ')
    if roll_no[:3]=='B23' and len(roll_no)==6 and marks <=100 and marks >0:
        student=ic152(name,roll_no,marks)
        print(student.check())
        
    else:
        print('Invalid input')
except:
    print('Invalid input')