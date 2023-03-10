# This is a script to help export screenshots into Blender from DOSBox, PCem, etc.

# Required Libraries: global-hotkeys, pypiwin32, pyautogui, pillow

from global_hotkeys import *
import pyautogui
import time

is_alive = True  # Flag to indicate to the program whether it should continue running.


def take_screenshot():
    game_location = pyautogui.locateOnScreen('checkPositionWith.png')
    print(game_location)
    pyautogui.screenshot('screenshot.png')


def exit_application():
    global is_alive
    stop_checking_hotkeys()
    is_alive = False


bindings = [  # [<key list>, <keydown handler callback>, <keyup handler callback>]
    [["print_screen"], None, take_screenshot],
    [["control", "print_screen", "shift"], None, exit_application],
]


register_hotkeys(bindings)  # Register all of our keybindings
start_checking_hotkeys()    # Start listening for keypresses


while is_alive:  # Run until closed
    time.sleep(0.1)
