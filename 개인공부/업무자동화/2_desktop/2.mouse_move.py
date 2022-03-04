import pyautogui

# 절대좌표
# pyautogui.moveTo(200, 100)
# pyautogui.moveTo(100, 200, duration=3)
# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)

# 상대좌표, 현재 커서 위치로부터
# pyautogui.moveTo(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())

# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())


# print(pyautogui.position())

p = pyautogui.position()
print(p.x, p.y)
