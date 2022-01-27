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

if not os.path.isdir('images_png'):
    os.mkdir('images_png')
else:
    pass

if not os.path.isdir('images_jpg'):
    os.mkdir('images_jpg')
else:
    pass


def get_image():
    random_url = [random.choice('qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOP1234567890' if i != 5 else '')
                  for i in range(5)]
    imgur = 'https://i.imgur.com/'

    random_url_jpg = [random.choice('qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOP1234567890' if i != 5 else '')
                      for i in range(5)]

    x = imgur + str(''.join(random_url)) + '.png'
    y = requests.get(x)
    z = str(''.join(random_url)) + '.png'

    x2 = imgur + str(''.join(random_url_jpg)) + '.jpg'
    y2 = requests.get(x2)
    z2 = str(''.join(random_url_jpg)) + '.jpg'

    out = open("images_png/" + z, "wb")
    out.write(y.content)
    out.close()

    out2 = open("images_jpg/" + z2, "wb")
    out2.write(y2.content)
    out2.close()

    im = Image.open("images_png/" + z)
    (width, height) = im.size
    im.close()

    im2 = Image.open("images_jpg/" + z2)
    (width2, height2) = im2.size
    im2.close()

    if width == 161 and height == 81:
        os.remove("images_png/" + z)
        print('[INVALID.PNG] --> ' + x)
    else:
        print('[VALID.PNG] --> ' + x)

    if width2 == 161 and height2 == 81:
        os.remove("images_jpg/" + z2)
        print('[INVALID.JPG] --> ' + x2)
    else:
        print('[VALID.JPG] --> ' + x2)


global delay
try:
    delay = int(input('[INPUT] Enter delay between checking 1 image in seconds (min. 1) >'))
except ValueError:
    print('[ERROR] Not a number!')
    input('Press enter to exit...')
    exit()
print('[INFO] Starting!')
try:
    while True:
        get_image()
        time.sleep(delay)
except KeyboardInterrupt:
    print('[INFO] Stopped!')
    input('Press enter to exit...')
    exit()
