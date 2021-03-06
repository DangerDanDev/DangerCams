import cv2 as cv
import PIL.Image, PIL.ImageTk
from typing import Union
import typing
import numpy

class Camera:

    input_source: cv.VideoCapture

    def get_width(self):
        """
        The width of the frame that will be returned from self.get_frame() and associated methods. It is a good
        idea to match this number to the size of the container displaying the video.
        """
        return self.__width

    def get_height(self):
        """
        The height of the frame that will be returned from self.get_height() and associated methods.
        It is a good idea to match this number to the size of the container displaying the video.
        :return:
        """
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def __init__(self, input_src, width=-1, height=-1):
        
        # Get a video capture opject from OpenCV
        self.input_source = cv.VideoCapture(input_src)
        
        if width == -1:
            self.set_width(self.input_source.get(cv.CAP_PROP_FRAME_WIDTH))
        else:
            self.set_width(width)
                      
        if height == -1:
            self.set_height(self.input_source.get(cv.CAP_PROP_FRAME_HEIGHT))
        else:
            self.set_height(height)

    def __del__(self):
        self.input_source.release()

    def get_frame(self) -> (bool, numpy.ndarray):
        # Trying to do frame-work on an invalid stream is a bad idea. Best to just skip it
        # So the rest of the program can work.
        if self.input_source.isOpened():

            # Get the raw frame from the camera and a bool flag telling
            # us if it was read correctly
            ret, frame = self.input_source.read()

            if ret:
                # We want to return the frame in the size I have been set to
                frame = cv.resize(frame, (int(self.__width), int(self.__height)))

                return ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            else:
                return ret, None

    def get_photo_image(self) -> tuple[bool, PIL.ImageTk.PhotoImage]:

        # Get the frame from cv.VideoInput
        ret, frame = self.get_frame()

        # We only assign a value to this photo if a frame was successfully read
        photo = None

        # If a frame was read, convert it to a tkinter PhotoImage and assign it to variable photo
        if ret and frame is not None:
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

        # If there was no frame returned, set our success boolean to false
        elif frame is None:
            ret = False

        # Return whether the operation succeeded and the photo, whether or not it is 'None'
        return ret, photo
