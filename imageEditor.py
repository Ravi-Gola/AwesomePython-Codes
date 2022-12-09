import cv2
#reading image
image = cv2.imread("apple.jpg")
#converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#image inversion(for enhance the details of image)
inverted_image = 255 - gray_image

# convert this inverted image in blurr image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# blurred image inversion
inverted_blurred = 255 - blurred

# convert image to pencil sketch image by dividing gray_image by inverted_blurred image
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# for show image
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch ", pencil_sketch)
cv2.waitKey(0)