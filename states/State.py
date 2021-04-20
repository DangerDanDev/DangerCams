import tkinter

class State:
    """
    A base class for program states. States determine
    """

    def is_in_state(self) -> bool:
        """

        :return: True if this is the active state of the program, false
        if it is not.
        """
        return self.__in_state

    def __init__(self):
        self.__in_state = False

    def enter_state(self, frame: tkinter.Frame):
        """
        Sets the __in_state flag to true so we can see that this is the active state
        :param frame: The frame where I will place a canvas with camera feed
        :return: None
        """

        self.__in_state = True

    def exit_state(self, frame: tkinter.Frame):
        """
        Sets the __in_state flag to false so we can tell that this is not the active state!
        :param frame:
        :return:
        """
        self.__in_state = False

    def update(self, frame: tkinter.Frame):
        """
        Updates the frame so we can pull dimensions as needed
        :param frame:
        :return:
        """
        frame.update()

    def draw(self, frame: tkinter.Frame):
        """

        :param frame:
        :return:
        """
        pass

    def override_on(self, frame: tkinter.Frame):
        """
        NOT IMPLEMENTED YET.
        Should use rasberry Pi interface to turn on the car screen override toggle,
        forcing the car to display app input
        :param frame:
        :return:
        """
        pass

    def override_off(self, frame: tkinter.Frame):
        """
        NOT IMPLENTED YET
        Will use Rasberry Pi interface to turn off the screen override, allowing the car to show the regular backup camera
        :param frame:
        :return:
        """
        pass