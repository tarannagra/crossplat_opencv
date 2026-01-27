import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./assets/orna.png")

if image is None:
    raise Exception("Could not find image")

colours = ("b", "g", "r")


for channel, colour in enumerate(colours):
    hist = cv2.calcHist(
        [image],
        [channel],
        None,
        [256],
        [0,256]
    )
    plt.plot(hist, color=colour)

plt.title("RGB Histograms")
plt.xlabel("Pixel Value")
plt.ylabel("Count")
print("Displaying the histogram...")
plt.show()

# this code works! now write it up
