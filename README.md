# Optical Flow Estimation using Lucas-Kanade Method ( MOTION TRACKING )

This program demonstrates optical flow estimation using the Lucas-Kanade method in OpenCV. Optical flow is a computer vision technique that tracks the motion of objects in a video sequence.

## Description

The program starts by reading a video file and converting the frames to grayscale. It then applies the Lucas-Kanade algorithm to estimate the optical flow between consecutive frames.

The Lucas-Kanade parameters, such as the window size and termination criteria, are set to control the accuracy and performance of the optical flow estimation. The program also utilizes the 'cv2.goodFeaturesToTrack' function to find initial feature points for tracking.

Once the optical flow is computed, the program visualizes the estimated motion by drawing lines and circles on the frames. These visualizations help understand the direction and magnitude of the object's movement.

The program uses a while loop to process each frame of the video, and it terminates when the 'q' key is pressed. Afterward, the video capture is released, and all windows are closed.

## Prerequisites
   Python 3.x
   OpenCV library
   NumPy library
   
## Usage
Clone this repository to your local machine or download the source code files.

Make sure you have Python 3.x and the required libraries installed.

Place your video file in the same directory as the source code files.

Update the 'cap = cv2.VideoCapture('walking.mp4')' line with the path or filename of your video file.

Run the program.

The video window will display the frames with the overlay of estimated optical flow.

Press the 'q' key to stop the program and close the windows.

## OUTPUT 
![im](https://github.com/VEERA-3/MOTION_TRACKING/assets/88039094/200b6351-ff5c-4216-96ad-0a867c75c9d8)
