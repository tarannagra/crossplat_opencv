import cv2
import time
import numpy as np

# Create large image
img = np.random.randint(0, 255, (4000, 4000, 3), dtype=np.uint8)

start = time.time()
for _ in range(100):
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
print(f"Time: {time.time() - start:.2f}s")
