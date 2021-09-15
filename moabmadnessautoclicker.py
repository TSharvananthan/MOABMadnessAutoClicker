import pyautogui
from time import sleep

pyautogui.FAILSAFE = True


sleep(1)
pyautogui.click(x = 222 , y = 165)

while True:
    pyautogui.click(x = 638 , y = 414)
    sleep(5)
    pyautogui.click(x = 1231 , y = 535)
    pyautogui.click(x = 514 , y = 296)
    pyautogui.click(x = 1009 ,y = 905)
    pyautogui.click(x = 1009 ,y = 905, clicks = 4)
    pyautogui.click(x = 1231 , y = 535)
    pyautogui.click(x = 536 , y = 459)
    pyautogui.click(x = 1009 ,y = 905, clicks = 4)

    pyautogui.press("space")
    pyautogui.press("space")

    sleep(10)
    pyautogui.click(x = 52 ,y = 778)
    sleep(8)
    pyautogui.click(x = 52 ,y = 778)
    sleep(4)
    pyautogui.click(x = 155 ,y = 189)
    sleep(5)
