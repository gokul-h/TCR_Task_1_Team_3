# TCR Task 1 Goal 2
# Integrate the module developed during goal 1 in a
# web interface (can use flask).

from flask import Flask, render_template, Response
# Importing our python code as module
from ball_tracking import DetectGreenBall

# initialize a flask object
app = Flask(__name__)


# Render the index.html template
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
def index():
    return render_template('index.html')


# The gen() function enters a loop where it continuously returns frames from the camera as response chunks.
# The function asks the camera to provide a frame by calling the camera.
def gen(ball):
    while True:
        # Get frames
        frame = ball.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Provides video feed to frontend
@app.route('/video_feed')
def video_feed():
    # The class we made is being imported here which automatically invokes constructors and the function
    # It also uses the function gen() to get frames
    return Response(gen(DetectGreenBall()), mimetype='multipart/x-mixed-replace; boundary=frame')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

# Note:
# 1. Multiple Browser windows not supported ()

# Resources
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
# https://blog.miguelgrinberg.com/post/video-streaming-with-flask/page/8#:~:text=The%20mimetype%20argument%20is%20set,frame%20by%20calling%20the%20camera.
# https://www.geeksforgeeks.org/python-yield-keyword/#:~:text=yield%20is%20a%20keyword%20in,is%20what%20makes%20a%20generator.
# https://www.geeksforgeeks.org/flask-creating-first-simple-application/#:~:text=Flask%20is%20a%20web%20application,Both%20are%20Pocco%20projects.
# https://www.reddit.com/r/learnpython/comments/3l242p/what_this_code_belongs_to_from_a_camera_streaming/
# https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal