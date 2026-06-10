markdown_content = """# Edge Detection from Scratch: Matrix Convolution

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-Core_Logic-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-I/O-red.svg)

## 📌 Overview

This project is an implementation of fundamental image processing algorithms—specifically edge detection—built from scratch. Instead of relying on black-box library functions like `cv2.Sobel()` or `cv2.Canny()`, this script manually implements the sliding-window matrix convolution necessary to extract high-frequency features (edges) from digital images.

It demonstrates a strong, hands-on understanding of the linear algebra and computational mathematics that power modern computer vision frameworks.

## ✨ Features

- **Custom Convolution Engine:** Implements a raw $3 \\times 3$ sliding window algorithm to calculate image gradients without abstracting the core mathematics.
- **Multiple Operators:** Easily swappable kernels for different edge detection strategies:
  - **Sobel Operator:** Emphasizes center pixels for noise reduction.
  - **Prewitt Operator:** Uniform weight distribution for standard gradient extraction.
- **Magnitude Calculation:** Computes the Euclidean distance of $G_x$ and $G_y$ gradients ($G = \\sqrt{G_x^2 + G_y^2}$).
- **Binary Thresholding:** Converts continuous gradient magnitudes into crisp, binary edge maps.
- **Side-by-Side Visualization:** Uses Matplotlib to render the original grayscale input alongside the calculated edge map.

## 🧮 The Mathematics

An image is treated as a 2D matrix of pixel intensities. Edges are located by finding areas of rapid intensity change using derivatives. This is approximated via convolution with specific kernels.

**The Sobel Kernels:**
Vertical Edges ($G_x$):
$$\\begin{bmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{bmatrix}$$

Horizontal Edges ($G_y$):
$$\\begin{bmatrix} 1 & 2 & 1 \\\\ 0 & 0 & 0 \\\\ -1 & -2 & -1 \\end{bmatrix}$$

## 🚀 Getting Started

### Prerequisites

You will need Python 3 installed along with a few standard scientific libraries.
