import tkinter

import PIL

import CameraCanvas
from Camera import Camera


class App:
    window: tkinter.Tk = tkinter.Tk()

    def __init__(self):

        self.delay = 5

        self.window.title('Webcam test!')

        # Uncomment this on my desktop to load a camera from a pre-saved video file
        # self.camera = Camera(r'C:\Users\scyth\Documents\Programming\PythonDemos\pexels-how-far-from-home-5592502.mp4')

        # Uncomment this to load a camera from the webcam on my laptop
        self.camera = Camera(0)

        self.canvas = CameraCanvas.CameraCanvas(self.window, self.camera, 100, 125)
        self.canvas.pack()

        self.update()
        self.window.mainloop()

    def update(self):

        self.canvas.update()

        self.window.after(self.delay, self.update)

