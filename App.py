import tkinter

import PIL

from Camera import Camera


class App:
    window: tkinter.Tk = tkinter.Tk()

    def __init__(self):

        self.delay = 5

        self.window.title('Webcam test!')

        self.camera = Camera(r'C:\Users\scyth\Documents\Programming\PythonDemos\pexels-how-far-from-home-5592502.mp4')

        self.canvas = tkinter.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.update()
        self.window.mainloop()

    def update(self):
         """ret, frame = self.camera.get_frame()

         if ret:
             self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

         self.window.after(self.delay, self.update)"""

         ret, self.photo = self.camera.get_photo_image()

         if ret:
            self.canvas.create_image(0,0, image=self.photo, anchor=tkinter.NW)

