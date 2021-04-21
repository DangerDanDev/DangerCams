import tkinter

import PIL

import CameraCanvas
from Camera import Camera

from ButtonWindow import ButtonWindow
from states.SingleCameraState import SingleCameraState
from states.State import State


class App:

    # Main app window
    window: tkinter.Tk = tkinter.Tk()

    # A list of camera manager states
    __states = []

    __frame = tkinter.Frame(window, width=640, height=480)

    # A list of each camera input screen
    __states = list()

    # The camera input that is currently displayed
    __state_index = - 1

    def next_camera(self):
        self.state.enter_state(self.__frame)

    def __init__(self):

        # The time between video frame updates (in milliseconds)
        self.delay = 5

        # Set the title and size of the window
        self.window.geometry('640x480')
        self.window.title('DANGER Cams')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.init_cameras()

        self.__frame.grid(row=0,column=0)
        self.__frame.grid_columnconfigure(0, weight=1)
        self.__frame.grid_rowconfigure(0, weight=1)

        self.buttonWindow = ButtonWindow(self.window.master, btn_callback=self.next_state)
        self.window.mainloop()

    def init_cameras_no_webcam(self):
        self.__states.append(SingleCameraState(frame=self.__frame,source=r'C:\Users\scyth\Videos\video1.mp4',
                                        width = 640, height = 480))

        self.__states.append(SingleCameraState(frame=self.__frame, source=r'C:\Users\scyth\Videos\video2.mp4',
                                               width=640, height=480))
    def init_cameras(self):
        # print valid indices

        for i in range(0,2):
            self.__states.append(SingleCameraState(frame=self.__frame, source=i, width=640, height=480))

    def next_state(self):

        print('Going to next state')

        # We only exit the old state if it is a valid state
        if self.__state_index >= 0:
            old_state: State = self.__states[self.__state_index]
            old_state.exit_state(self.__frame)

        # Go to the next state, or loop back to zero if applicable
        self.__state_index = (self.__state_index + 1) % len(self.__states)
        new_state: State = self.__states[self.__state_index]
        new_state.enter_state(self.__frame)
        new_state.update(self.__frame)