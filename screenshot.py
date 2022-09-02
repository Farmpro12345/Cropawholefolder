from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

i = 1
while i < 6:

    keyboard.press(Key.print_screen)
    keyboard.press(Key.alt)

    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    keyboard.release(Key.print_screen)
    keyboard.release(Key.alt)


    time.sleep(2)
    keyboard.press(Key.down)
    keyboard.release(Key.down)


