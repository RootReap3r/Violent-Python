import pynput
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

activity_buffer = []
BUFFER_THRESHOLD = 20


def on_key_press(key):
    global activity_buffer
    try:
        # Log the alphanumeric key pressed
        activity_buffer.append(str(key.char))
    except AttributeError:
        # Log special key pressed
        activity_buffer.append(str(key))
    if len(activity_buffer) >= BUFFER_THRESHOLD:
        write_buffer()


def on_click(x, y, button, pressed):
    global activity_buffer
    if pressed:
        activity_buffer.append(f"Mouse clicked at ({x},{y}) with {button}")
        if len(activity_buffer) >= BUFFER_THRESHOLD:
            write_buffer()


def write_buffer():
    global activity_buffer
    with open("log.txt", "a") as f:
        for item in activity_buffer:
            f.write(item + '\n')
    activity_buffer = []


def on_key_release(key):
    if key == Key.esc:
        write_buffer()  # Write remaining activities from buffer
        return False


# Separate listeners for keyboard and mouse
keyboard_listener = KeyboardListener(on_press=on_key_press, on_release=on_key_release)
mouse_listener = MouseListener(on_click=on_click)

with keyboard_listener as kl, mouse_listener as ml:
    kl.join()
    ml.join()

