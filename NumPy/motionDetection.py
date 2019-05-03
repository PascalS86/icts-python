import sys
import cv2
import time
import numpy as np

#setup video capture
if len(sys.argv) < 2:
    capture = cv2.VideoCapture(0)
else:
    file = sys.argv[1]
    capture = cv2.VideoCapture(file)


# Read two frames, last and current, and convert current to gray.
ret, lastFrame = capture.read()
ret, currentFrame = capture.read()
gray = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)

while True:
    lastFrame = currentFrame
    ret, currentFrame = capture.read() #read the next frame

    if not ret: #if no image is captured, break
        break
    
    #get the gray value and compare the last two frames, by getting the absolute difference between the arrays
    gray = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(lastFrame, currentFrame)

    print("Current frame = ", np.mean(currentFrame))
    print("Diff = ", np.mean(diff))

    #if the difference is higher, than a natural noise, we print out, motion detected
    if np.mean(diff) > 5:
        print("Motion detected")

    cv2.imshow("Camera Image", diff)
    time.sleep(0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'): #quit capturing
        break

capture.release()
cv2.destroyAllWindows()
