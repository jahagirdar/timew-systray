import threading
import pystray
import asyncio
import subprocess
import time
from PIL import Image, ImageDraw


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(
    'test name',
    icon=create_image(64, 64, 'black', 'white'))


threading.Thread(target=icon.run).start()
# To finally show you icon, call run
#icon.run_detached()
on_img=Image.open('timew_on.png')
off_img=Image.open('timew_off.png')
while True:
    tw=subprocess.run(['timew'],capture_output=True)
    if tw.returncode==0:
        #icon.icon=create_image(64, 64, 'black', 'green')
        icon.icon=on_img
    else:
        #icon.icon=create_image(64, 64, 'black', 'red')
        icon.icon=off_img
    icon.notify(message=str(tw.stdout))
    time.sleep(600)
