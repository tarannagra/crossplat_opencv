import cv2
import numpy as np
import matplotlib.pyplot as plt

# Code taken from ../Image_Transformations_Demo.ipynb and put into its own file due to no Jupyter
# Learn and evaluate this code to see how it does what it does

# Reading the image
img = cv2.imread("../assets/orna.png", 0)

# Loading the image
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

# Translation
M=np.float32([[1,0,50],[0,1,30]])
out=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
plt.imshow(out,cmap="gray")
plt.axis("off")
plt.show()

# Rotation
c=(img.shape[1]//2,img.shape[0]//2)
M=cv2.getRotationMatrix2D(c,45,1)
out=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
plt.imshow(out,cmap="gray")
plt.axis("off")
plt.show()

# Reflection
out=cv2.flip(img,1)
plt.imshow(out,cmap="gray") 
plt.axis("off")
plt.show()

# Fourier Transform
f=np.fft.fftshift(np.fft.fft2(img))
mag=20*np.log(np.abs(f)+1)
plt.imshow(mag,cmap="gray")
plt.axis("off")
plt.show()

# Frequency Filtering
rows,cols=img.shape
crow,ccol=rows//2,cols//2
mask_lp=np.zeros_like(img)
mask_lp[crow-30:crow+30,ccol-30:ccol+30]=1
mask_hp=1-mask_lp
f_lp=f*mask_lp
f_hp=f*mask_hp
lp=np.abs(np.fft.ifft2(np.fft.ifftshift(f_lp)))
hp=np.abs(np.fft.ifft2(np.fft.ifftshift(f_hp)))
fig,ax=plt.subplots(1,2); ax[0].imshow(lp,cmap="gray")
ax[0].axis("off")
ax[1].imshow(hp,cmap="gray")
ax[1].axis("off")
plt.show()
