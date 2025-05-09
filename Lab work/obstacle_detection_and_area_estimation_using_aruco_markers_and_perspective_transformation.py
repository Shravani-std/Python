
import cv2
import numpy as np

# Load the image
image = cv2.imread('/content/3dbce88e-4eb3-4ffb-a9b4-d010abd21ff6.jpeg')

# Define the Aruco dictionary and parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Detect markers
corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(image, aruco_dict, parameters=parameters)

# Draw detected markers
cv2.aruco.drawDetectedMarkers(image, corners, ids)

if ids is not None:
    # Assuming you want to use the first four detected markers
    src_points = []
    for corner in corners:
        src_points.append(corner[0])
    src_points = np.array(src_points[:4], dtype='float32')  # Take first four markers
else:
    # Handle the case where no markers are detected, potentially by assigning a default image
    print("No AruCo markers detected.")
    # Example: Use the original image as a fallback
    transformed_image = image  # Or you can use a placeholder image
    # ... (Rest of your code to handle the fallback case)

if ids is not None:
    # Assuming you want to use the first four detected markers
    # Convert corners to a NumPy array before reshaping
    corners_np = np.array(corners)  # Convert corners (tuple) to a NumPy array
    src_points = corners_np.reshape(-1, 2).astype(np.float32)[:4]

    # Define destination points (adjust based on your requirements)
    width, height = 640, 480
    dst_points = np.array(
        [[0, 0], [width, 0], [width, height], [0, height]], dtype="float32"
    )

    # Get the perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply the transformation
    transformed_image = cv2.warpPerspective(image, matrix, (width, height))
else:
    print("No AruCo markers detected.")
    # Example: Use the original image as a fallback
    transformed_image = image  # Or you can use a placeholder image
    # ... (Rest of your code to handle the fallback case)

# Define destination points (adjust based on your requirements)
width, height = 640, 480
dst_points = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype='float32')

# Get the perspective transformation matrix
if ids is not None and len(src_points) == 4:
  matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply the transformation
  transformed_image = cv2.warpPerspective(image, matrix, (width, height))
else:
  print("Not Enough Markers detected to perform perspective transformation")
  # Example: Use the original image as a fallback
  transformed_image = image  # Or you can use a placeholder image
  # ... (Rest of your code to handle the fallback case)

gray = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # Example thresholding

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

min_area = 1000
for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_area:  # Filter out small areas
        cv2.drawContours(transformed_image, [contour], -1, (0, 255, 0), 2)  # Draw contours
        print(f'Obstacle area: {area}')

from google.colab.patches import cv2_imshow
output_image = np.zeros_like(transformed_image)

# Fill the output image with detected obstacles
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # Filter small areas
        cv2.drawContours(output_image, [contour], -1, (255, 255, 255), -1)  # Draw filled contours in white

# Display the final output image with only obstacles
cv2.imshow(output_image)

from google.colab.patches import cv2_imshow # Import cv2_imshow from google.colab.patches
import cv2

scale_factor = 0.5  # Adjust this factor as needed (0.5 will reduce the size to half)
small_transformed_image = cv2.resize(transformed_image, (0, 0), fx=scale_factor, fy=scale_factor)
# Save the transformed image with reduced quality
cv2.imwrite('transformed_image.jpg', small_transformed_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # Adjust the quality (0-100)

cv2_imshow(small_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()