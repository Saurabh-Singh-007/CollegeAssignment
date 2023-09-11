rows=int(input("Enter the number of rows"))
columns=int(input("Enter the number of columns"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range (columns):
        row.append(input("Enter the element for ("+str(i+1)+","+str(j+1)+")"))
    matrix.append(row)

for m in matrix:
    print(m)

k=int(input("Enter the number you want to search :"))
rowIndex=-1
columnIndex=-1
for n in range(0,len(matrix)):
    for o in range(0,len(matrix[n])):
        if(matrix[n][o]==k):
            rowIndex=n
            columnIndex=o
            break


if(rowIndex!=-1) :      
    print(rowIndex+1)
    print(columnIndex+1)
else:
    print("Not found")

            




