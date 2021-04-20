from states.State import State
import tkinter
from Camera import Camera


class SingleCameraState(State):

    canvas: tkinter.Canvas
    photo_image: tkinter.PhotoImage

    def __init__(self, source: str):
        State()

        self.source = source
        self.photo_image = tkinter.PhotoImage(file=self.source)

    def enter_state(self, frame: tkinter.Frame):
        State.enter_state(self)

        self.canvas = tkinter.Canvas(frame)  # Maybe set width and height?
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=tkinter.NW)
        # self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.canvas.grid(row=0, column=0)

    def exit_state(self, frame: tkinter.Frame):
        State.exit_state(self, frame)
        self.canvas.pack_forget()
