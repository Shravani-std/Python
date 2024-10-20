
# import imageio.v3 as iio
import numpy as np
from skimage import io as ski   #convert img in ndarray
import matplotlib.pyplot as plt   #show img

img1 = ski.imread('/content/Screenshot (16).png')
print(img1)

plt.imshow(img1)
plt.show()

print("Shape of img ",img1.shape)
print("Dimension of img ",img1.ndim)

img1[:,:,0]
# img1[:,:,0].shape
# img1[:,:,0].ndim

"""represent rgb values in range of 0-1"""

img_array = img1 / 255
print(img_array)

img_array.min()
# img_array.max()

img_array.dtype

"""we can assign each color channel to a separate matrix using the slice syntax"""

# red_array = img_array[:,:,0]
# green_array = img_array[:,:,1]
# blue_array = img_array[:,:,2]

"""Operations on Axis"""

from numpy import linalg as la

img_rgb = img_array[:, :, :3]

img_gray = np.dot(img_rgb, [0.2126, 0.7152, 0.0722])

img_gray.shape

plt.imshow(img_gray,cmap="gray")
plt.show()

"""Apply SVD"""

U,s,Vt = la.svd(img_gray)

U.shape,s.shape,Vt.shape

import numpy as np

Sigma = np.zeros((U.shape[1] , Vt.shape[0]))
np.fill_diagonal(Sigma,s)

"""Approximation"""

la.norm(img_gray - U @ Sigma @ Vt)

np.allclose(img_gray, U @ Sigma @ Vt)

plt.plot(s)
plt.show()

k = 10
aprroximation = U @ Sigma[:,:k] @ Vt[:k,:]
plt.imshow(aprroximation,cmap="gray")
plt.show()

"""Apply all colors"""

img_array.shape

"""SO we want (4,768,1366) so we use transpose"""

img_array_transposed = np.transpose(img_array, (2, 0, 1))
img_array_transposed.shape

#Apply svd again on new transposed img
U, s, Vt = la.svd(img_array_transposed)

U.shape, s.shape, Vt.shape

for i in range(img_array_transposed.shape[0]):
    U, s, Vt = la.svd(img_array_transposed[i, :, :])


    Sigma = np.zeros((img_array_transposed.shape[1], img_array_transposed.shape[2]))  # shape (768, 1024)
    np.fill_diagonal(Sigma, s)


    reconstructed_channel = U @ Sigma @ Vt

    if i == 0:
        reconstructed = np.zeros_like(img_array_transposed)

    reconstructed[i, :, :] = reconstructed_channel


reconstructed.shape

reconstructed.min(), reconstructed.max()

reconstructed = np.clip(reconstructed, 0, 1)
plt.imshow(np.transpose(reconstructed, (1, 2, 0)))
plt.show()

approx_img = U @ Sigma[..., :k] @ Vt[..., :k, :]
approx_img.shape

plt.imshow(np.transpose(approx_img, (0,1,2)))
plt.show()