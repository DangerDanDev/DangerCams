import tkinter

class ButtonWindow:
    """
    A window that displays a clickable button that triggers display cycling
    on the main app window. It is used to simulate the physical button in a testing environment
    """

    __window: tkinter.Toplevel

    btn_next_camera: tkinter.Button

    def __init__(self, parent: tkinter.Tk, btn_callback):

        self.__window = tkinter.Toplevel(parent)

        self.btn_next_camera = tkinter.Button(master=self.__window, text='Next camera', command=btn_callback)
        self.__window.grid_rowconfigure(0, weight=1)
        self.__window.grid_columnconfigure(0, weight=1)
        self.btn_next_camera.grid(row=0, column=0)

        self.__window.mainloop()

    def next_camera(self):
        print('next camera function not implemented yet')
