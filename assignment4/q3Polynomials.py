# ls=eval(input("Enter the list :"))
# n=int(input("Enter the degree"))
# def coefficient(n):
#     return ls[n-1]
# print(coefficient(n))



# def function (x):
#     return 4*(x**3)-6*(x**2)-1
# print(function(int(input("Enter the number x :"))))



n1=int(input("Enter the degree of 1st polynomial"))
ls_1=[]
for i in range (0,n1+1):
    ls_1.append(int(input("Enter the coefficient of x^"+str(i))))

n2=int(input("Enter the degree of 2nd polynomial"))
ls_2=[]
for j in range (0,n2+1):
    ls_2.append(int(input("Enter the coefficient of x^"+str(j))))
#adds polynomials
l=[]
if (n1>n2):
    for i in range (0,n1-n2):
        l.append(ls_1[i])
    k=0
    for j in range (n1-n2,n1+1):
        l.append(ls_1[j]+ls_2[k])
        k+=1
elif(n2>n1):
    for l in range (0,n2-n1):
        l.append(ls_1[l])
    m=0
    for n in range (n2-n1,n2+1):
        l.append(ls_1[n]+ls_2[m])
        m+=1
else:
    for o in range (0,n1):
        l.append (ls_1[o]+ls_2[o])
print(l)


             
        

        
    
        



