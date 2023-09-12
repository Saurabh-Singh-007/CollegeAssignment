ls=eval(input("Enter the list"))
l=[]
for element in range (0,len(ls)):
    l.append(max(ls))
    ls.remove(max(ls))
print(l)

