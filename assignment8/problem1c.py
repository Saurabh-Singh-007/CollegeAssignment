from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})


# install pillow using:
# pip3 install pillow
# if above does not work and you are on windows, try:-
# py -m pip3 install pillow

# importing Image and ImageOps from PIL
from PIL import Image, ImageOps

# creating image object:
imInp = Image.open('problem1cInput.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
import numpy as np
pixels2D = np.array(imGrayscale)
print(pixels2D.shape)

# showing/saving image
# imGrayscale.show()
imGrayscale.save('problem1cOutput.jpg')

# Write code for finding histogram here:
plt.hist(pixels2D.flatten())
plt.xlabel("Value of Pixels")
plt.ylabel("Frequency")
plt.title("Histogram of Pixels")
plt.savefig("problem1ci.png")
plt.show()

# Write code for finding histogram of difference of pixel's intensity
# with its left neighbour here:
diff=[]
for row in pixels2D:
    for i in range(len (row)):
        if i==0 :
            diff.append(row[i])
        else:
            diff.append(int(row[i])-int(row[i-1]))
xaxis=[i for i in range (min(diff),max(diff),20)]
plt.hist(diff,bins=20)
plt.xlabel("Difference of consecutive pixels")
plt.xticks(xaxis,fontsize=10)
plt.ylabel("Frequency")
plt.title("Histogram of difference of pixels")
plt.savefig("problem1cii.png")
plt.show()