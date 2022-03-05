import pyautogui

# img = pyautogui.screenshot()
# img.save('screenshot.png')

# pyautogui.mouseInfo()
# 23, 17 50, 165, 241  # 32A5F1

pix = pyautogui.pixel(23, 17)
print(pix)

print(pyautogui.pixelMatchesColor(23, 17, pix))
print(pyautogui.pixelMatchesColor(23, 17, pix))
