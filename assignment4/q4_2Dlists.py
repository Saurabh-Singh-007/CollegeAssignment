# rows=int(input("Enter the number of rows"))
# columns=int(input("Enter the number of columns"))
# matrix=[]
# for i in range(rows):
#     row=[]
#     for j in range (columns):
#         row.append(input("Enter the element for ("+str(i+1)+","+str(j+1)+")"))
#     matrix.append(row)

# for m in matrix:
#     print(m)

# k=int(input("Enter the number you want to search :"))
# rowIndex=-1
# columnIndex=-1
# for n in range(0,len(matrix)):
#     for o in range(0,len(matrix[n])):
#         if(matrix[n][o]==str(k)):
#             rowIndex=n
#             columnIndex=o
#             break


# if(rowIndex!=-1) :      
#     print("Found at (row,column) = ("+str(n+1)+","+str(o+1)+")")
# else:
#     print("Not found")



import math

rows=int(input("Enter the number of rows"))
columns=int(input("Enter the number of columns"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range (columns):
        row.append(input("Enter the element for ("+str(i+1)+","+str(j+1)+")"))
    matrix.append(row)


if rows==columns:
    n=rows
    count=0
    count_s=0
    for i in range(0,rows):
        for j in range(0,columns):
            if matrix[i][j]==matrix[j][i]:
                count+=1
    if count ==math.pow(n,2):
        print("It is symmetric matrix")
    else:
        print("It is not a symmetric matrix")
    
    for k in range(0,rows):
        for l in range(0,columns):
            if int(matrix[i][j])==int((int(matrix[j][i]))*(-1)):
                count_s+=1
    if count_s==math.pow(n,2):
        print("It is a skew symmetric matrix")
    else:
        print("It is not a skew symmetric matrix")


            




