# TCR Task 1 Goal 1
# Develop a python module to take visual feed from
# the camera and detect the green ball in the feed.

# import the necessary packages
import cv2
from imutils import grab_contours

# Define the lower and upper boundaries of the "green"
# ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# Capture the Video (Video Capture)
# 0 --> Webcam Video
# 1 --> If using Droid cam /other sources
# File location if Saved Video


class DetectGreenBall(object):
    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()

    def get_frame(self):
        while True:
            # p_area is initialised to zero since if in a frame no contour is detected
            # the loop to calculate p_area will not be executed which will throw an error
            global p_area
            p_area = 0
            # Boolean to store if frames are present or not
            isTrue, frame = self.video.read()

            # Blur Each frame to enhance detection
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)

            # Since default colorspace of OpenCV is BGR convert it into HSV
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            # Construct a mask for the color "green"
            mask = cv2.inRange(hsv, greenLower, greenUpper)

            # Perform a series of dilations and erosions to
            # remove any small blobs left in the mask
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            # Show the masked video
            # cv2.imshow("Masked Feed", mask)

            # Find contours in the mask
            contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

            # findContour function return 2 or 3 values depending on the version
            # Since we only need contours we use grab_contours() from imutils
            contours = grab_contours(contours)

            # Only proceed if at least one contour was found
            if len(contours) > 0:
                # find the largest contour in the mask
                c = max(contours, key=cv2.contourArea)
                # Draw the Rectangle in each frame for largest contour
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Find the area of current rectangle
                rect_area = w * h
                # Find total area
                total_area = frame.shape[0] * frame.shape[1]
                # Find the percentage of area covered
                p_area = (rect_area / total_area) * 100
                
            # To print the value in the frame itself
            new = cv2.putText(frame, str(p_area), (50, 50),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA, False)

            # To filter out small errors in detection
            # To print the values in python console
            if p_area >= 1:
                print(f'Percentage of area is {p_area}')

            # Encode OpenCV raw frame to jp and display it
            ret, jpeg = cv2.imencode(".jpg", new)
            return jpeg.tobytes()

# Requirements
# 1.The ball should be be the largest green object in the video
# 2.It can only detect one ball at a time
# Reason:
# The algorithm works in such a way that it detects the largest
# green object, mask it ad draws rectangle

# Sources/Reference
# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# https://youtu.be/oXlwWbU8l2o
# https://docs.opencv.org/master/d9/d8b/tutorial_py_contours_hierarchy.html
# https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
# https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163#39201163
