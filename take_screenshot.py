import numpy as np
import pyautogui
import imutils
import cv2
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image)),
cv2.imwrite("in_memory_to_disk.png")
pyautogui.screenshot("straight_to_disk.png")
image = cv2.imread("straight_to_disk.png")
cv2.imshow("Scrrenshot, imutils.resize(image.width=600")