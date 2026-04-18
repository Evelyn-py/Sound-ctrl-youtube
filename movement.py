import keyboard
import pyautogui



class MovieMovement:
    def __init__(self):
        self.keyboard_press = lambda key: keyboard.press_and_release(key)
        self.pyautogui = pyautogui.press

    def pause(self):
        return self.keyboard_press('space')

    def forward(self):
        return self.pyautogui('right', presses=2)

    def backward(self):
        return self.pyautogui('left', presses=3)

    def full_screen(self):
        return self.keyboard_press('f')

    def exit_full_screen(self):
        return self.keyboard_press('esc')

    def next(self):
        return self.keyboard_press('shift+N')


class DisplaySetting:
    def louder(self):
        return pyautogui.press('volumeup', presses=3)

    def softer(self):
        return pyautogui.press('volumedown', presses=3)

    def slide_down(self):
        return pyautogui.scroll(100)

    def slide_up(self):
        return pyautogui.scroll(-100)






