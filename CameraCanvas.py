import tkinter
import PIL.Image, PIL.ImageTk
import cv2

from Camera import Camera


class CameraCanvas(tkinter.Canvas):

    #
    __camera: Camera

    __image: tkinter.PhotoImage

    def get_camera(self) -> Camera:
        return self.__camera

    def __init__(self, master, camera: Camera, width=-1, height=-1):
        """
        :param master: My master widget, inherited from tkinter.Canvas.__init__()
        :param camera: The camera feed whose video I display.
        :param width: The width of this canvas. -1 means
            leave the feed as is, any other value will set the width of the camera feed.
        :param height: The height of this canvas. -1 Will leave the height as the size of the
            camera feed, any other value will set it accordingly.
        """
        if width == -1:
            width = camera.get_width()
        else:
            camera.set_width(width)

        if height == -1:
            height = camera.get_height()
        else:
            camera.set_height(height)

        # We still need to init as a regular canvas
        tkinter.Canvas.__init__(self, master=master, width=width, height=width)

        # Init the read only variable
        self.__camera = camera

    def update(self):
        # Call this to ensure the widget's width and height are updated
        tkinter.Canvas.update(self)

        # Get the frame from the camera
        ret, self.__image = self.__camera.get_photo_image()

        if ret:
            self.create_image(0, 0, image=self.__image, anchor=tkinter.NW)
