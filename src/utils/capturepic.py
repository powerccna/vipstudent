#!/usr/bin/env python
# encoding: utf-8
from PIL import ImageGrab

def capture_screen(name):
    pic = ImageGrab.grab()
    rgb_im = pic.convert('RGB')
    rgb_im.save(name+'.jpg')