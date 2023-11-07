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
