import tkinter


class State:
    """
    A base class for program states. States determine
    """
    def __init__(self):
        pass

    def enter_state(self):
        pass

    def exit_state(self, frame: tkinter.Frame):
        pass

    def update(self, frame: tkinter.Frame):
        pass

    def draw(self, frame: tkinter.Frame):
        pass

    def override_on(self, frame: tkinter.Frame):
        pass

    def override_off(self, frame: tkinter.Frame):
        pass