import tkinter

class State:
    """
    A base class for program states. States determine
    """

    def is_in_state(self) -> bool:
        return self.__in_state

    def __init__(self):
        self.__in_state = False

    def enter_state(self, frame: tkinter.Frame):
        frame.update()

        self.__in_state = True

    def exit_state(self, frame: tkinter.Frame):
        self.__in_state = False

    def update(self, frame: tkinter.Frame):
        frame.update()

    def draw(self, frame: tkinter.Frame):
        pass

    def override_on(self, frame: tkinter.Frame):
        pass

    def override_off(self, frame: tkinter.Frame):
        pass