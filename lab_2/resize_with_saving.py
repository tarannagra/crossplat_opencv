import cv2 as cv
import matplotlib.pyplot as plt

# Code taken from ../Resize_Demo_with_Saving.ipynb and put into its own file due to no Jupyter
# Learn and evaluate this code to see how it does what it does

# Reading image
img=cv.imread("../assets/orna.png",0)

down_nearest=cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_NEAREST)
cv.imwrite("down_nearest.png",down_nearest)

down_linear=cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_LINEAR)
cv.imwrite("down_linear.png",down_linear)

down_cubic=cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)
cv.imwrite("down_cubic.png",down_cubic)

up_nearest=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_NEAREST)
cv.imwrite("up_nearest.png",up_nearest)

up_linear=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_LINEAR)
cv.imwrite("up_linear.png",up_linear)

up_cubic=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
cv.imwrite("up_cubic.png",up_cubic)

plt.figure(figsize=(10,6))
plt.subplot(2,3,1)
plt.imshow(down_nearest,cmap="gray")
plt.show()

plt.title("50% Nearest")
plt.axis("off")
plt.subplot(2,3,2)
plt.imshow(down_linear,cmap="gray")
plt.show()

plt.title("50% Linear")
plt.axis("off")
plt.subplot(2,3,3)
plt.imshow(down_cubic,cmap="gray")
plt.show()

plt.title("50% Cubic")
plt.axis("off")
plt.subplot(2,3,4)
plt.imshow(up_nearest,cmap="gray")
plt.show()

plt.title("200% Nearest")
plt.axis("off")
plt.subplot(2,3,5)
plt.imshow(up_linear,cmap="gray")
plt.show()

plt.title("200% Linear")
plt.axis("off")
plt.subplot(2,3,6)
plt.imshow(up_cubic,cmap="gray")
plt.show()

plt.title("200% Cubic")
plt.axis("off")
plt.tight_layout()
plt.show()
