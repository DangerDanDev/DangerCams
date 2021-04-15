import tkinter

import PIL

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

        self.canvas = tkinter.Canvas(self.window, width=self.camera.get_width(), height=self.camera.get_height())
        self.canvas.pack()

        self.update()
        self.window.mainloop()

    def update(self):

         ret, self.photo = self.camera.get_photo_image()

         if ret:
            self.canvas.create_image(0,0, image=self.photo, anchor=tkinter.NW)

            self.window.after(self.delay, self.update)

