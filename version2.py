# This is a script to help export screenshots into Blender from DOSBox, PCem, etc.

# Required Libraries: global-hotkeys, pypiwin32, pyautogui, pillow

from global_hotkeys import *
import pyautogui
import time

is_alive = True  # Flag to indicate to the program whether it should continue running.


def take_screenshot():
    pyautogui.screenshot('my_screenshot.png')


def up_action():
    print('up_action pressed')


def down_action():
    print('down_action pressed')


def left_action():
    print('left_action pressed')


def right_action():
    print('right_action pressed')


def exit_application():
    global is_alive
    stop_checking_hotkeys()
    is_alive = False


bindings = [  # [<key list>, <keydown handler callback>, <keyup handler callback>]
    [["print_screen"], None, take_screenshot],
    [["up"], None, up_action],
    [["down"], None, down_action],
    [["left"], None, left_action],
    [["right"], None, right_action],
    [["control", "print_screen", "shift"], None, exit_application],
]


register_hotkeys(bindings)  # Register all of our keybindings
start_checking_hotkeys()    # Start listening for keypresses


while is_alive:  # Run until closed
    time.sleep(0.1)
