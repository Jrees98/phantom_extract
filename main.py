from PIL import Image
import pytesseract


image_path = 'phantom_4.jpeg'
img = Image.open(image_path)

text = pytesseract.image_to_string(img)

# Open a file in write mode ('w')
with open('output.txt', 'w') as file:
    file.write(text)

# The file will be automatically closed when the 'with' block is exited


print(text)
