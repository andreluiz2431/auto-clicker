import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 1.0
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
        self.clicks = []

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def add_click(self, position, button):
        self.clicks.append((position, button))

    def play_sequence(self):
        for position, button in self.clicks:
            mouse.position = position
            mouse.click(button)
            time.sleep(self.delay)

    def run(self):
        while self.program_running:
            while self.running:
                self.play_sequence()
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay)
click_thread.start()

set_position_key = KeyCode(char='w')
left_click_key = KeyCode(char='z')
right_click_key = KeyCode(char='x')
play_sequence_key = KeyCode(char='q')

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
    elif key == set_position_key:
        global last_position
        last_position = mouse.position
    elif key == left_click_key:
        click_thread.add_click(last_position, Button.left)
    elif key == right_click_key:
        click_thread.add_click(last_position, Button.right)
    elif key == play_sequence_key:
        if not click_thread.running:
            click_thread.start_clicking()

with Listener(on_press=on_press) as listener:
    listener.join()