from matplotlib import pyplot as plt
import numpy as np


def circle(size,centre=0,boundary=128):
    kernel_2D = 255*np.ones((size,size))
    kernel_2D[size//2,size//2] = centre
    centre = size//2
    for i in range(size):
        for j in range(size):
            radius=((centre-i)**2+(centre-j)**2)**0.5
            if(radius<=size//2):
                kernel_2D[i,j]=radius

    histList=[]
    for i in range(size):
        for j in range(size):
            if kernel_2D[i,j] <= 255: histList.append(kernel_2D[i,j])
            
    plt.subplot(1,2,1)

    plt.imshow(kernel_2D, interpolation='bilinear',cmap='gray')
    plt.title("Image")

    plt.subplot(1,2,2)
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixel count")
    plt.grid(True)
    plt.xlim([0.0, 250.0])  # <- named arguments do not work here
    plt.hist(kernel_2D.flatten(), bins = boundary//2+1,color='#0504aa',
                                alpha=0.7, rwidth=0.6, align='mid', density=True)
    plt.tight_layout()

    figure = plt.gcf() # get current figure
    figure.set_size_inches(16, 12)
    plt.show() 
    plt.savefig('problem1bOp.jpg', bbox_inches='tight')# change this to problem1bOp.png
    return kernel_2D

circle(255)
