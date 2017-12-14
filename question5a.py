import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plot_image_histogram(img1,title1,H1,title2,img3,title3,H2,title4):
    plt.subplot(221)
    plt.imshow(img1, cmap=cm.gray)
    plt.title(title1)

    plt.subplot(222)
    plt.hist(H1)
    plt.title(title2)

    plt.subplot(223)
    plt.imshow(img3, cmap=cm.gray)
    plt.title(title3)

    plt.subplot(224)
    plt.hist(H2)
    plt.title(title4)
    plt.show()




img = Image.open("question5.jpg") # Opened image
I = np.asarray(img) # saved it in matrix
w,h=I.shape

H = np.zeros(256)
for i in range(256):
    H[i]=np.sum(I==i)

H=H/(w*h)

p=H.copy()
sum=0

for i in range(256):
    p[i]=p[i]+sum
    sum=p[i]


g=np.floor(255*p)

out = I.copy()

for i in range(256):
    out[I==i] = g[i]


H1 = np.zeros(256)
for i in range(256):
    H1[i]=np.sum(out==i)

plot_image_histogram(I,"Original Image",H,"Original Histogram",out,"After Image",H1,"After Histogram")