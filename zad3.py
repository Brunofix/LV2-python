import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

img= img+50
img=np.rot90(img, k=1)

print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")

plt.show()