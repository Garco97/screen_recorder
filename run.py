import pyautogui
import numpy as np
import cv2
FPS = 60
SECONDS = 1
SCREEN_SIZE = pyautogui.Size(width=1920, height=1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, FPS, (SCREEN_SIZE))
print(pyautogui.size())
print(type(pyautogui.size()))

frames = []
for i in range(SECONDS * FPS):
    # make a screenshot
    img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    frames.append(img)
    # convert these pixels to a proper numpy array to work with OpenCV
    
for img in frames:
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)


# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()