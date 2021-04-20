from states.State import State
import tkinter
from Camera import Camera
from tkinter import N, S, E, W
from PIL.Image import Image
from PIL.ImageTk import  PhotoImage


class SingleCameraState(State):

    canvas: tkinter.Canvas

    def __init__(self, source: str):
        State()

        self.source = source
        self.original_image = tkinter.PhotoImage(file=self.source)

    def enter_state(self, frame: tkinter.Frame):
        State.enter_state(self, frame)

        self.canvas = tkinter.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height())  # Maybe set width and height?

        self.canvas.create_image(0, 0, image=self.original_image, anchor=tkinter.NW)
        self.canvas.grid(row=0, column=0)

    def exit_state(self, frame: tkinter.Frame):
        State.exit_state(self, frame)
        self.canvas.pack_forget()
