import pyautogui; import time
class write:
    def __init__(self, word, delay, count):
        self.word = word
        self.delay = delay
        self.count = count
        time.sleep(float(delay))
        for i in range(int(count)):
            pyautogui.write(word)
            pyautogui.press("enter")
write("kakas", 4, 2)
