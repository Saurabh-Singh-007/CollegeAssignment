import matplotlib.pyplot as plt
import sys

def isNum(value) :
    if value[0] in '+-' : value = value[1 :]
    return value.isdigit()

n=len(sys.argv)-1

if len(sys.argv)==1:
    print("Not a valid path , please provide a valid path")

for i in range(1,n+1):
    try:
        file_path=sys.argv[i]
        xValues=[]
        yValues=[]         # try block to catch exceptions
        with open(file_path,'r') as file:
            for line in file:
                print(line)
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
                
                
                    plt.scatter(xValues,yValues)
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.title('Scatter Plot')
                    plt.show()
    
    
    except FileNotFoundError:    # exception for file not found
        print("Invalid path")

    except Exception :       # exception for any other error while processing the file
        print("An error occured while opening or processing the file")
