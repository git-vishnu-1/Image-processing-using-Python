import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'batman.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

sobel_x = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])
sobel_y = np.array([[1,2,1],
                   [0,0,0],
                   [-1,-2,-1]])

rows, cols = img.shape
edge_magnitude = np.zeros((rows, cols))

for i in range(1,rows - 1):
    for j in range(1, cols - 1):
        patch = img[i-1:i+2, j-1:j+2]

        gx = np.sum(patch * sobel_x)
        gy = np.sum(patch * sobel_y)

        magnitude = np.sqrt(gx**2 + gy**2)
        edge_magnitude[i,j] = magnitude

threshold = 100
final_edge = np.where(edge_magnitude > threshold, 255, 0)

plt.figure(figsize = (10,5))

plt.subplot(1,2,1)
plt.title("Orginal Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Detected Edges")
plt.imshow(final_edge, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()