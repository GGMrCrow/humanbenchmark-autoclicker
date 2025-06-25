import pyautogui as pag
import time

# RGB Values for the colors on the humanbenchmark reaction test
BLUE = (43, 135, 209)
GREEN = (75, 219, 106)

# Loop
while True:
    color = pag.screenshot().getpixel((595, 427))  # Getting pixel color from screen
    if color == GREEN:
        pag.click(595, 427)
    elif color == BLUE:
        time.sleep(1)  # Just to see the result     
        pag.click(595, 427)
