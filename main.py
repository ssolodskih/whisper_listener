import threading
import time

import keyboard
import pyautogui
import pyperclip
from dotenv import load_dotenv

from recognition import recognize

load_dotenv()


def recognize_callback(result):
    # This function will be called with the result of `recognize`
    pyperclip.copy(result)  # Copy result to clipboard
    time.sleep(0.1)  # Short delay to ensure clipboard is updated
    pyautogui.hotkey('command', 'v')  # Paste content


def recognize_wrapper():
    # This function wraps the call to `recognize` and handles its output
    result = recognize()  # Assume this function returns the text to be pasted
    recognize_callback(result)  # Pass the result to the callback function


def on_hotkey_pressed():
    print("Hotkey pressed, activating...")
    threading.Thread(target=recognize_wrapper).start()  # Use the wrapper function


if __name__ == "__main__":
    # Set the hotkey to whatever you prefer

    keyboard.add_hotkey('command+f1', on_hotkey_pressed)  # Example: Pressing 'ctrl' and 'alt' together activates the recording

    print("Listening for hotkey...")

    keyboard.wait('esc')  # Use 'esc' key to stop listening (or any key of your choice)
