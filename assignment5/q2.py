import matplotlib.pyplot as plt


def f(n):
    if n<2:
        return 1
    else:
        return 1.65*f(n-1)
    

def g(n):
    if n<2:
        return 1
    else:
        return g(n-1)+g(n-2)
    

def h(n):
    if n<2:
        return 2
    else:
        return 2*h(n-2)
    

def k(n):
    if n<3:
        return 3
    else:
        return k(n-1)+k(n-3)
    

x=[]
y=[]
z=[]
o=[]
j=[]
for i in range(0,10):
    x.append(f(i))
    y.append(g(i))
    z.append(h(i))
    o.append(k(i))
    j.append(i)


plt.scatter(j,x,color='red',label='f(n)')
plt.show()

plt.scatter(j,y,color='blue',label='g(n)')
plt.show()

plt.scatter(j,z,color='green',label='h(n)')
plt.show()

plt.scatter(j,o,color='black',label='k(n)')
plt.show()




plt.scatter(j,x,color='red',label='f(n)')


plt.scatter(j,y,color='blue',label='g(n)')


plt.scatter(j,z,color='green',label='h(n)')


plt.scatter(j,o,color='black',label='k(n)')
plt.legend()
plt.show()


print("f(n) grows exponentially")
print("g(n) is fibonacci sequence")
print("h(n) doubles for even n while remaining constant for odd n")
print("k(n) is a sequence that adds the previous 2 odd numbers to the previous even number")

