# Import the main libraries used in the project
import cv2
import pytesseract

# Reading an image
img = cv2.imread('test.jpg')

# Converting image as Tesseract accepts RGB value and OpenCV accepts BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Printing characters recognised in the image in the form of a group of strings
print(pytesseract.image_to_string(img))

# Detecting each and every characters
height, width, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for box in boxes.splitlines():
    box = box.split(' ')
    print(box)

# Draw the rectangles around the characters
for box in boxes.splitlines():
    box = box.split(' ')
    x = int(box[1])
    y = int(box[2])
    w = int(box[3])
    h = int(box[4])
    cv2.rectangle(img, (x,height-y), (w,height-h), (0,0,255), 1)

# Putting text on the image
for box in boxes.splitlines():
    box = box.split(' ')
    x = int(box[1])
    y = int(box[2])
    cv2.putText(img, box[0], (x,height-y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)

# Loading the image
cv2.imshow('Result', img)
cv2.waitKey(0)