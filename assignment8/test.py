#code to write input file of 1000000 sorted random numbers
import random
with open ("problem2Input.txt","w") as f:
    f.write(str((random.randint(1,1000000)))+"\n")
    for i in range (1000000):
        f.write(str(i)+" ")