import cv2
import pytesseract

img_path = "static/image3.jpg"

# Read the image file
image = cv2.imread(img_path)

# Run OCR on the image
text = pytesseract.image_to_string(image, lang='eng')

# Print the extracted text
print(text)