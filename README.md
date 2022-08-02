# Sobel Edge Detection
## Description
Edge detection is a technique of image processing used to identify points in a digital image with discontinuities, simply to say, sharp changes in the image brightness. These points where the image brightness varies sharply are called the edges (or boundaries) of the image. Design and implement a program that will organize and save an edge detection image using the “Sobel edge detection” method. I should mention that when implementing the program, the corresponding functions should not be called, but implemented.

## Prerequisites
* Python
* NumPy
* Matplotlib
* OpenCV

## Algorithm
To implement the Sobel Edge Detection we should:

* load the image
* gray the image
* convolute the image by $x$ direction using Sobel Operator
* convolute the image by $y$ direction using Sobel Operator
* combine convolutions

Sobel Operators are used to see how much is the difference between pixels. So, if it's great enough it can be considered as an edge.
Sobel Operators:

$$
G_x=
\begin{bmatrix}
1 & 0 & -1\\
2 & 0 & -2\\
1 & 0 & -1\\
\end{bmatrix};
G_y=
\begin{bmatrix}
1 & 2 & -1\\
0 & 0 & 0\\
-1 & -2 & -1\\
\end{bmatrix}
$$

To combine the convolutions:

$$G=\sqrt{G_x^2+G_y^2}$$

## Results

The implementation with comments is shown in [ipynb](sobel-edge-detection.ipynb) file.

The original image:
![Result](./src/img/image.jpg)

Edge Detection:
![Result](./src/img/image_gradient_mag.jpg)
