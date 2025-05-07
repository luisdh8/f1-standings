import cv2
import easyocr
import re
import numpy as np

img_path = 'Assets/Japan - Feature.png'
original = cv2.imread(img_path)

# Filter white
img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
lower_white = np.array([140, 140, 140])
upper_white = np.array([255, 255, 255])

mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        r, g, b = img[y, x]
        if (lower_white[0] <= r <= upper_white[0] and
            lower_white[1] <= g <= upper_white[1] and
            lower_white[2] <= b <= upper_white[2]):
            mask[y, x] = 255

# Gaussian filter
blurred = cv2.GaussianBlur(mask, (3, 3), sigmaX=2)

# Separate black and white
_, binary = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

# Kernel 3x3
kernel = np.ones((3, 3), np.uint8)

# Erotion & Dilatation
cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)

# Gaussian filter 2
blurred2 = cv2.GaussianBlur(cleaned, (3, 3), sigmaX=2)

# Separate black and white 2
_, binary2 = cv2.threshold(blurred2, 150, 255, cv2.THRESH_BINARY)

# Erotion & Dilatation 2
cleaned2 = cv2.morphologyEx(binary2, cv2.MORPH_OPEN, kernel, iterations=1)

# Read the image
reader = easyocr.Reader(['en'])
results = reader.readtext(cleaned2, paragraph=False)

# Filter the pilots' names
pilots = []
for (bbox, text, confidence) in results:
    (tl, tr, br, bl) = bbox
    tl = tuple(map(int, tl))
    br = tuple(map(int, br))
    cv2.rectangle(original, tl, br, (0, 255, 0), 2)
    cv2.putText(original, text, tl, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    if re.match(r'^[A-Za-z]{3,}$', text):
        pilots.append(text.upper())

for name in pilots:
    print(name)

# Show all the images
cv2.imshow("Image", original)
cv2.imshow("Mask", mask)
cv2.imshow("Blurred", blurred)
cv2.imshow("Cleaned", cleaned)
cv2.imshow("Blurred 2", blurred2)
cv2.imshow("Cleaned 2", cleaned2)
cv2.waitKey(0)
cv2.destroyAllWindows()