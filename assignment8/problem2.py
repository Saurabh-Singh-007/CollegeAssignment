import sys
if len(sys.argv) != 2:
    print("Usage: python3 problem2.py <filename>")
    exit()
fileName=sys.argv[1]

try:
    with open (fileName,"r") as f :
        lines=f.readlines()
except:
    print("File not found")
    exit()


value=int(lines[0].strip())
arr = [int(i) for i in lines[1].split()]

def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1



def linearSearch(arr,value):
    for element in arr:
        if element==value:
            return arr.index(element)
    return -1

#comparing time for linear and binary search
import time
start=time.time()
linearSearch(arr,value)
end=time.time()
print("Time taken for linear search is ",end-start)

start=time.time()
binary_search(arr,value)
end=time.time()
print("Time taken for binary search is ",end-start)

