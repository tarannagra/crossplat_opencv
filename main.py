import cv2

img = cv2.imread(filename="./assets/orna.png")
# cv2.imshow("Displayed Image", img)
print(f"Index at [10][10]: {img[10][10]}")

h, w, c = img.shape

out = img.copy()


for x in range(h):
    for y in range(w):
        blue = out[x, y, 0]
        green = out[x, y, 1]
        red = out[x, y, 2]

        # perform the swap...
        out[x, y, 0] = red # r -> b
        out[x, y, 2] = blue # b -> r
        
