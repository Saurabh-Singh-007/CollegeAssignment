import numpy as np
import sys

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
    
for i in range(1,len(sys.argv)):
    filepath=sys.argv[i]
    with open(filepath,'r') as f:
            l=f.readlines()
            x=l[0].split()
            y=l[1].split()
            x1=[]
            y1=[]
            for i in range(1,len(x)):
                if is_int(x[i]):
                    x1.append(int(x[i]))
                
            for i in range(1,len(y)):
                if is_int(y[i]):
                    y1.append(int(y[i]))

            x1=np.array(x1)
            y1=np.array(y1)
            xmean=np.mean(x1)
            ymean=np.mean(y1)
            x=x1-xmean
            y=y1-ymean
            rNum=np.sum(x*y)        #dot product of x and y
            rDen=np.sqrt(np.sum(np.square(x))*np.sum(np.square(y)))   #product of magnitude of x and y
            r=rNum/rDen
            print(r)

            #finding r using the formula
            rnum=(len(x1)*np.sum(x1*y1))-(np.sum(x1)*np.sum(y1))
            rden=np.sqrt((len(x1)*np.sum(np.square(x1))-np.square(np.sum(x1)))*(len(y1)*np.sum(np.square(y1))-np.square(np.sum(y1))))
            r=rnum/rden
            print(r)
            

            

                