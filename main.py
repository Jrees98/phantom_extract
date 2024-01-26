from PIL import Image
import pytesseract

# Open an image file
image_path = 'phantom_1.jpeg'
img = Image.open(image_path)

# Use pytesseract to extract text
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
