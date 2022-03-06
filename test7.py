import keyboard
import time


def aaa():
    try:
        time.sleep(2)
        print(1/0)
    except:
        return

    try:
        time.sleep(10)
        print(1/0)
    except:
        return


def bbb():
    print('b')


keyboard.add_hotkey('q', aaa)
keyboard.add_hotkey('w', bbb)


while True:
    keyboard.read_key()
