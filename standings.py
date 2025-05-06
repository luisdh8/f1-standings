import cv2
import numpy as np
import easyocr

img_path = 'Assets/Australia - Feature.png'

original = cv2.imread(img_path)
img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

lower_white = np.array([120, 120, 120])
upper_white = np.array([255, 255, 255])

# # Filter black
# mask = np.zeros(gray.shape, dtype=np.uint8)

# for y in range(gray.shape[0]):
#     for x in range(gray.shape[1]):
#         value = gray[y, x]
#         if value < 50:
#             mask[y, x] = 255

# # Gaussian filter
# blurred = cv2.GaussianBlur(mask, (21, 21), sigmaX=9)

# Filter white
mask = np.zeros(img.shape, dtype=np.uint8)

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        r, g, b = img[y, x]
        if (lower_white[0] <= r <= upper_white[0] and
            lower_white[1] <= g <= upper_white[1] and
            lower_white[2] <= b <= upper_white[2]):
            mask[y, x] = 255

# OCR
reader = easyocr.Reader(['en'])
results = reader.readtext(mask)

for (bbox, text, confidence) in results:
    (tl, tr, br, bl) = bbox
    tl = tuple(map(int, tl))
    br = tuple(map(int, br))
    cv2.rectangle(original, tl, br, (0, 255, 0), 2)
    cv2.putText(original, text, tl, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    print(f"Detected: '{text}' with confidence {confidence:.2f}")


cv2.imshow("Original", original)
# cv2.imshow("Mask", mask)
# cv2.imshow("Gaussian", blurred)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()