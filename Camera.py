import cv2 as cv
import PIL.Image, PIL.ImageTk
from typing import Union

class Camera:

    input_source: cv.VideoCapture

    def get_width(self):
        """
        Width is assigned in the constructor
        and should only be read from after that
        :return:
        """
        return self.__width

    def get_height(self):
        """
        Returns the read-only (from outside) variable '__height'
        :return:
        """
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def __init__(self, input_src):

        self.input_source = cv.VideoCapture(input_src)

        self.__width = self.input_source.get(cv.CAP_PROP_FRAME_WIDTH)
        self.__height = self.input_source.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        self.input_source.release()

    def get_frame(self):
        if self.input_source.isOpened():

            ret, frame = self.input_source.read()

            frame = cv.resize(frame, (int(self.__width), int(self.__height)))
            print('Width: ', self.__width, 'Height: ', self.__height)

            if ret:
                return ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            else:
                return ret, None

    def get_photo_image(self) -> tuple[bool, PIL.ImageTk.PhotoImage]:

        ret, frame = self.get_frame()

        photo = None

        if ret:
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

        return ret, photo