from states.State import State
import tkinter
from CameraCanvas import CameraCanvas
from Camera import Camera


class SingleCameraState(State):

    __canvas: CameraCanvas
    __camera: Camera


    def __init__(self, frame, source: str, width, height):
        State()

        self.__camera = Camera(input_src=source, width=width, height=height)

        self.source = source

    def enter_state(self, frame: tkinter.Frame):

        # avoid throwing errors after the program closes
        if not frame.winfo_exists():
            return

        #
        State.enter_state(self, frame)

        # Turn on the reverse override to trigger the car's screen
        # to show this display
        self.override_on()

        self.__canvas = CameraCanvas(frame, self.__camera, self.__camera.get_width(), self.__camera.get_height())
        self.__canvas.grid(column=0,row=0)



        self.update(frame)

    def update(self, frame: tkinter.Frame):
        State.update(self, frame=frame)

        self.__canvas.update()

        if self.is_in_state():
            frame.after(10, lambda: self.update(frame))


    def exit_state(self, frame: tkinter.Frame):
        State.exit_state(self, frame)
        self.__canvas.grid_forget()
        self.__in_state = False
