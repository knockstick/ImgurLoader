import time
import requests
from PIL import Image
import random
import os

logo = """
█ █▀▄▀█ █▀▀ █░█ █▀█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
█ █░▀░█ █▄█ █▄█ █▀▄ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄
"""
print(logo + '\nMade with <3 by knockstick')
print('\nNote: This program is made only for educational purposes. I am not responsible for any your actions.')

if not os.path.isdir('images'):
    os.mkdir('images')
else:
    pass

def get_image():
    random_url = [random.choice('qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOP1234567890' if i != 5 else '')
                  for i in range(5)]
    imgur = 'https://i.imgur.com/'

    x = imgur + str(''.join(random_url)) + '.png'
    y = requests.get(x)
    z = str(''.join(random_url)) + '.png'

    out = open("images/" + z, "wb")
    out.write(y.content)
    out.close()

    im = Image.open("images/" + z)
    (width, height) = im.size
    im.close()

    if width == 161 and height == 81:
        os.remove("images/" + z)
        print('[INVALID] --> ' + x)
    else:
        print('[VALID] --> ' + x)


global delay
try:
    delay = int(input('[INPUT] Enter delay between checking 1 image in seconds (min. 1) >'))
except ValueError:
    print('[ERROR] Not a number!')
    exit()
print('[INFO] Starting!')
try:
    while True:
        get_image()
        time.sleep(delay)
except KeyboardInterrupt:
    print('[INFO] Stopped!')
