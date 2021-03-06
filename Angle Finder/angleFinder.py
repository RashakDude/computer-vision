# Importing the libraries required in the project
from cv2 import cv2
import math

# Loading the image 
img = cv2.imread('test.jpg')

# Declaration of the points list array
points = []

# Function used to find the points clicked on the image and draw these points on the same image
def mousePoints (event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 5, (0,0,255), cv2.FILLED)
        points.append([x,y])
        # print(points)

# Function to find out the slope of the line between two points
def gradient(p1, p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

# Function to get the angle 
def getAngle (points):
    p1, p2, p3 = points[-3:]
    m1 = gradient(p1,p2)
    m2 = gradient(p1,p3)
    ang = math.atan(abs((m2-m1)/(1+(m2*m1))))
    print(round(math.degrees(ang)))

# Displaying the image
while True:
    if len(points)%3 == 0 and len(points) is not 0:
        getAngle(points)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        points = []
        img = cv2.imread('test.jpg')