import pyautogui

width, height = pyautogui.size()

pyautogui.FAILSAFE = False

pyautogui.moveTo(10, height - 10, duration=0.3)

pyautogui.click()
pyautogui.moveTo(10, height - 60, duration=0.3)
pyautogui.click()

pyautogui.moveTo(30, height - 110, duration=0.3)
pyautogui.doubleClick()
