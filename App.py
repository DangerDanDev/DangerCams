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
        self.camera = Camera(r'C:\Users\scyth\Documents\Programming\PythonDemos\pexels-how-far-from-home-5592502.mp4')
        # Uncomment this to load a camera from the webcam on my laptop
        # self.camera = Camera(0)

        self.camera2 = Camera(r'C:\Users\scyth\Documents\Programming\PythonDemos\pexels-how-far-from-home-5592502.mp4')
        # self.camera2 = Camera(1)

        self.canvas = CameraCanvas.CameraCanvas(self.window, self.camera, width=133, height=100)
        self.canvas.pack(side='top')

        self.canvas2 = CameraCanvas.CameraCanvas(self.window, self.camera2, width=133, height=100)
        self.canvas2.pack()

        self.update()
        self.window.mainloop()

    def update(self):

        self.canvas.update()
        self.canvas2.update()

        self.window.after(self.delay, self.update)

