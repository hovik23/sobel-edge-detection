# Edge detection is a technique of image processing used to identify points
# in a digital image with discontinuities, simply to say, sharp changes
# in the image brightness. These points where the image brightness varies sharply
# are called the edges (or boundaries) of the image. Design and implement a program
# that will organize and save an edge detection image using the “Sobel edge detection”
# method. I should mention that when implementing the program, the corresponding
# functions should not be called, but implemented.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/image.jpg')
fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax.set_title('Original Image')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.imshow(gray, cmap="gray")
ax.set_title('Grayscaled Image')

kernel_x = np.array(
[
    [1,0,-1],
    [2,0,-2],
    [1,0,-1]
])

kernel_y = np.array(
[
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
])

def padding(image, pad=2):
    new_shape = tuple(map(lambda i, j: i + j, image.shape, (pad, pad)))
    padded_image = np.zeros(new_shape, dtype=int)
    lower = int(pad/2)
    padded_image[lower:new_shape[0] - lower, lower:new_shape[1] - lower] = image
    return padded_image, (pad, pad)

def convolution(image, kernel, padding_size):
    convolved_image = np.zeros(tuple(map(lambda i, j: i - j, image.shape, (2, 2))))
    for i in range(image.shape[0] - padding_size[0]):
            for j in range(image.shape[1] - padding_size[1]):
                convolved_image[i][j] = np.sum(image[i:i + kernel.shape[0], j:j + kernel.shape[1]] * kernel)
    return convolved_image

padded_matrix, padding_size = padding(gray)
print('Padded matrix:\n', padded_matrix)
G_x = convolution(padded_matrix, kernel_x, padding_size)

fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.imshow(G_x, cmap="gray")
ax.set_title('Gradient Approximations (x)')

G_y = convolution(padded_matrix, kernel_y, padding_size)

fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.imshow(G_y, cmap="gray")
ax.set_title('Gradient Approximations (y)')

edges = np.sqrt(G_x**2 + G_y**2)

fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.imshow(edges, cmap="gray")
ax.set_title('Gradient Magnitude')
plt.imsave('src/img/image_gradient_mag.jpg', edges, cmap="gray")

gradients = np.arctan2(G_y, G_x)

fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.imshow(gradients, cmap="gray")
ax.set_title('Gradient Directions')
