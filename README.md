# Green Ball detecting using OpenCV and Flask

>##  Description:
>
>### This Project uses Python OpenCV and flask to detect a green ball and print the area covered by it.

### Table of Contents

1.How to install/use this Project
2.Result 
3.Limitations
4.Exhaustive list of technology stack used.
5.The team
6.Resources

## 1.How to install/use this Project

Requirements:

- Python 3
- Flask 
- OpenCV 2
- Imutils

Command to install the required packages

 ```python
pip install Flask
pip install opencv-python
pip install imutils
 ```

To run the project in browser (Flask):

```python
python app.py
```

 To run pure python code in terminal

```python
python ball_tracking_3.py
```

 To run python code for task 1

```python
python ball_detection.py
```

The folders static and templates along with app.py and ball_tracking.py  belongs to the Flask Task \
The file ball_tracking.py belongs to task 1 \
The file ball_tracking_3.py is pure python implementation of final project.

## Result
The project is able to detect green ball and print the area covered by it

## Limitations

1. Multiple Browser windows not supported ()
2. The ball should be be the largest green object in the video
3. It can only detect one ball at a time \
   Reason: \
   The algorithm works in such a way that it detects the largest
   green object, mask it ad draws rectangle
4. Need to update the script if want to track a ball of different color.

## Exhaustive list of technology stack used

- Python
- Flask
- OpenCV
- Imutils

## The team

| Members    |
| :--------- |
| 1. Jigyasa |
| 2. Shruthi |
| 3. Gokul   |

| Mentors     |
| :---------- |
| 1. Dushyant |
| 2. Koushiki |

## Resources:
1. https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
2. https://blog.miguelgrinberg.com/post/video-streaming-with-flask/page/8#:~:text=The%20mimetype%20argument%20is%20set,frame%20by%20calling%20the%20camera
3. https://www.geeksforgeeks.org/python-yield-keyword/#:~:text=yield%20is%20a%20keyword%20in,is%20what%20makes%20a%20generator.
4. https://www.geeksforgeeks.org/flask-creating-first-simple-application/#:~:text=Flask%20is%20a%20web%20application,Both%20are%20Pocco%20projects
5. https://www.reddit.com/r/learnpython/comments/3l242p/what_this_code_belongs_to_from_a_camera_streaming/
6. https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
7. https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
8. https://youtu.be/oXlwWbU8l2o
9. https://docs.opencv.org/master/d9/d8b/tutorial_py_contours_hierarchy.html
10. https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
11. https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163#39201163
12. https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
13. https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
14. https://github.com/Practical-CV/Color-Based-Ball-Tracking-With-OpenCV/blob/master/README.md


