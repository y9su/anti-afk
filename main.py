import time
import pyautogui

hours = int(input("Enter hours you want to be AFK for: "))
seconds = hours * 60 * 60
moveafter = 105 # move after each 1:45 minutes to prevent kick

print(f"\nNow starting AFK for {hours} hours")

def wkey():
    pyautogui.moveTo(959, 525, duration=5)
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')

for i in range(seconds):
    time.sleep(moveafter)
    wkey()
print(f"Finished!, you were AFK for {hours} hours!")
