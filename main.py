from recognition import recognize

import keyboard
import threading


def on_hotkey_pressed():
    print("Hotkey pressed, activating...")
    # Run your main function in a separate thread to avoid blocking
    threading.Thread(target=recognize).start()


if __name__ == "__main__":
    # Set the hotkey to whatever you prefer
    keyboard.add_hotkey('ctrl+alt', on_hotkey_pressed)  # Example: Pressing 'ctrl' and 'alt' together activates the recording

    print("Listening for hotkey...")
    keyboard.wait('esc')  # Use 'esc' key to stop listening (or any key of your choice)
