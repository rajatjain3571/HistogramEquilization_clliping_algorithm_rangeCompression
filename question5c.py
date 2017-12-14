import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

import matplotlib.cm as cm


def plot_image(img1,title1,img2,title2,img3,title3,img4,title4,img5,title5):
    plt.subplot(331)
    plt.imshow(img1, cmap=cm.gray)
    plt.title(title1)


    plt.subplot(332)
    plt.imshow(img2, cmap=cm.gray)
    plt.title(title2)

    plt.subplot(333)
    plt.imshow(img3, cmap=cm.gray)
    plt.title(title3)

    plt.subplot(334)
    plt.imshow(img4, cmap=cm.gray)
    plt.title(title4)

    plt.subplot(335)
    plt.imshow(img5, cmap=cm.gray)
    plt.title(title5)
    plt.show()

def range_compression(image,c):
    img = Image.open(image)  # Opened image
    I = np.asarray(img)  # saved it in matrix
    F=I.copy()
    for i in range(F.shape[0]):
        for j in range(F.shape[1]):
            F[i,j]=c*np.log10(1+F[i,j])
    return F

img = Image.open("question5.jpg")  # Opened image
F = np.asarray(img)  # saved it in matrix
out1=range_compression("question5.jpg",1)
out2=range_compression("question5.jpg",10)
out3=range_compression("question5.jpg",100)
out4=range_compression("question5.jpg",1000)

# choosing c as 1 is giving binary type image. Chosing c as 1000 distorted the image. Where c=10 is fine and c=100 is giving good result
# getting good result with c=100, large pixels are compressed by this algorithm

plot_image(F,"Before Clipping",out1,"After Range Compression(C==1)",out2,"After Range Compression(C==10)",out3,"After Range Compression(C==100)",out4,"After Range Compression(C==1000)")
