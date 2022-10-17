from pynput.mouse import Button , Controller
import time
mouse = Controller()

time.sleep(30)

while True:
    time.sleep(0.1)
    mouse.press(Button.left)