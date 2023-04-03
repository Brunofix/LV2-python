import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

h, w = img.shape
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")
plt.title("Original image")

brighter_img = np.clip(img * 2, 0, 1)
plt.figure()
plt.imshow(brighter_img, cmap="gray")
plt.title("svjetlija")


rotirana_img: ndarray = np.zeros((w, h))
for y in range(h):
    for x in range(w):
        rotated_y = x
        rotated_x = h - 1 - y
        rotirana_img[rotated_y, rotated_x] = img[y, x]
plt.figure()
plt.imshow(rotirana_img, cmap="gray")
plt.title("rotirana")

preslikana_slika = np.zeros((h,w))
for x in range(h):
    mirrored_x = h - 1 - x
    preslikana_slika[mirrored_x,:] = img[x,:]
plt.figure()
plt.imshow(preslikana_slika, cmap="gray")
plt.title("preslikanal")


plt.show()
