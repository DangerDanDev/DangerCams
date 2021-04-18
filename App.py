import tkinter

import PIL

import CameraCanvas
from Camera import Camera

from ButtonWindow import ButtonWindow

class App:
    window: tkinter.Tk = tkinter.Tk()

    def __init__(self):

        # The time between video frame updates (in milliseconds)
        self.delay = 5

        # Set the title and size of the window
        self.window.geometry('640x480')
        self.window.title('DANGER Cams')

        self.cameras = list()
        self.camera_canvases = list()

        for i in range(0,4):
            self.add_camera(r'C:\Users\scyth\Documents\Programming\PythonDemos\pexels-how-far-from-home-5592502.mp4')

        # leftmost camera takes up the left third of the screen
        self.camera_canvases[0].grid(column=0, row=0, rowspan=2)

        # Middle 2 cameras split (top/bottom) the middle third of the screen
        self.camera_canvases[1].grid(column=1, row=0)
        self.camera_canvases[2].grid(column=1, row=1)

        # The right camera takes the right third of the screen
        self.camera_canvases[3].grid(column=2, row=0, rowspan=2)

        # Configure all grid columns to grow proportionally with the window
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

        # All grid rows should grow proportionally as well
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)

        self.update()

        self.buttonWindow = ButtonWindow(self.window.master)
        self.window.mainloop()



    def update(self):

        # If the window is not open, we do not want to update the
        # canvases or the video streams
        if not self.window.winfo_exists():
            return

        for canvas in self.camera_canvases:
            canvas.update()

        self.window.after(self.delay, self.update)

    def add_camera(self, camera_input: str):
        camera = Camera(camera_input)
        self.cameras.append(camera)
        self.camera_canvases.append(CameraCanvas.CameraCanvas(self.window, camera))