#use recursion to reverse capitalize a string
def prefRevCapStr(str):
    if len(str) == 0:
        return str
    else:
        return prefRevCapStr(str[1:]).upper()+str[0].upper()
str=input("Enter a string: ")
print(prefRevCapStr(str)+"->"+str)


#check for scattered substring
def scatSubStr(w,s):
    if len(w) == 0:
        return True
    elif w[0] in s:
        return scatSubStr(w[1:],s[s.index(w[0])+1:])
    else:
        return False

s=input("Enter a string: ")
w=input("Enter a word: ")
if scatSubStr(w,s):  
    print("Yes")
    print("Scattered substring "+w+" exists in the string")
else:
    print("No")


