from numpy import roots as r, round , real_if_close
n=int(input("Enter the degree of polynomial"))
ls=[]
for i in range (n,-1,-1):
    ls.append(int(input("Enter the coefficient of x^"+str(i))))
l=r(ls)
lis=[]

for element in l:
    lis.append((round((element))))
print(lis)



