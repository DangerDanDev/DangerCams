import cv2 as cv
import PIL.Image, PIL.ImageTk
from typing import Union

class Camera:

    input_source: cv.VideoCapture

    def __init__(self, input_src):

        self.input_source = cv.VideoCapture(input_src)

        self.width = self.input_source.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.input_source.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        self.input_source.release()

    def get_frame(self):
        if(self.input_source.isOpened()):

            ret, frame = self.input_source.read()

            if ret:
                return ret, cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            else:
                return ret, None

    def get_photo_image(self) -> tuple[bool, PIL.ImageTk.PhotoImage]:

        ret, frame = self.get_frame()

        photo = None

        if ret:
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

        return ret, photo