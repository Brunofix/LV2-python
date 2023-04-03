import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

h, w = img.shape
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")
plt.title("Original image")



rotated_img = np.zeros((w, h))
for y in range(h):
    for x in range(w):
        rotated_y = x
        rotated_x = h - 1 - y
        rotated_img[rotated_y, rotated_x] = img[y, x]

mirrored_img = np.zeros((w, h))
for y in range(w):
    for x in range(h):
        mirrored_x = h - 1 - x
        mirrored_img[y, mirrored_x] = rotated_img[y, x]




print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")

plt.show()