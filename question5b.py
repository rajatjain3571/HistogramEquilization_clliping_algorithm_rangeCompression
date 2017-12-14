import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def plot_image_histogram(img1,title1,img2,title2):
    plt.subplot(211)
    plt.imshow(img1, cmap=cm.gray)
    plt.title(title1)


    plt.subplot(212)
    plt.imshow(img2, cmap=cm.gray)
    plt.title(title2)
    plt.show()

img = Image.open("question5.jpg") # Opened image
I = np.asarray(img) # saved it in matrix
alpha=50
b=150
beta=2
F=I.copy()
for i in range(F.shape[0]):
    for j in range(F.shape[1]):
        if F[i,j]<50 and F[i,j]>=0:
            F[i,j]=0
        elif F[i,j]>=50 and F[i,j]<150:
            F[i,j]=2*(F[i,j]-50)
        elif F[i,j]>=150 and F[i,j]<256:
            F[i,j]=2*(b-alpha)

plot_image_histogram(I,"Before Clipping",F,"After Clipping")

#pixels are getting reduced
