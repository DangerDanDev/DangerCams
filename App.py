import tkinter

import PIL

import CameraCanvas
from Camera import Camera


class App:
    window: tkinter.Tk = tkinter.Tk()

    def __init__(self):

        self.delay = 5

        self.window.title('Webcam test!')

        self.cameras = list()
        self.camera_canvases = list()

        width = 133
        height = 100
        x = 0
        y = 0

        for i in range(0,4):
            self.cameras.append(Camera(r'C:\Users\scyth\Documents\Programming\PythonDemos\pexels-how-far-from-home-5592502.mp4'))
            self.camera_canvases.append(CameraCanvas.CameraCanvas(self.window, self.cameras[i], width=width, height=height))

        # leftmost camera takes up the left third of the screen
        self.camera_canvases[0].grid(column=0, row=0, rowspan=2)

        # Middle 2 cameras split (top/bottom) the middle third of the screen
        self.camera_canvases[1].grid(column=1, row=0)
        self.camera_canvases[2].grid(column=1, row=1)

        # The right camera takes the right third of the screen
        self.camera_canvases[3].grid(column=2, row=0, rowspan=2)

        self.update()
        self.window.mainloop()

    def update(self):

        for canvas in self.camera_canvases:
            canvas.update()

        self.window.after(self.delay, self.update)

