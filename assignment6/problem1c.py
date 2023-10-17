import matplotlib.pyplot as plt
import sys


def isNum(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


output=open("Output1c.txt","w")

if len(sys.argv)==1:
    print("No file path given, Please provide exact files")

n=len(sys.argv)-1

for i in range(1,n+1):
    try:
        file_path=sys.argv[i]
        
        xValues=[]
        yValues=[]         # try block to catch exceptions
        
        with open(file_path,'r') as file:
            for line in file:
                l=line.split()
                if l[0]=='x':
                    for i in range (1,len(l)):
                        l[i]=l[i].strip()
                        l[i]=l[i].rstrip()
                        if isNum(l[i]):
                            xValues.append(int(l[i]))
                        else:
                            print("Invalid file format : Character in file"+str(i))
                if l[0]=='y':
                    for i in range (1,len(l)):
                        if isNum(l[i]):
                            yValues.append(int(l[i]))
                        else:
                            print("Invalid file format : Character in file"+str(i))
            
            
            sum_x=sum(xValues)
            sum_y=sum(yValues)
            sum_xy=0
            sum_x2=0
            sum_y2=0
            for i in range(len(xValues)):
                sum_xy+=xValues[i]*yValues[i]
                sum_x2+=xValues[i]**2
                sum_y2+=yValues[i]**2
            n=len(xValues)
            r=(n*sum_xy-sum_x*sum_y)/(((n*sum_x2)-(sum_x)**2)**0.5)/((n*sum_y2)-(sum_y)**2)**0.5
            output.write(str(r)+' ')

    except FileNotFoundError:    # exception for file not found
        print("Invalid path")

    except Exception :       # exception for any other error while processing the file
        print("An error occured while opening or processing the file")


output.close()