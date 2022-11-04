# -*-coding:utf8;-*-
import requests
from qpycmd import droid
import torch
import time

menu = ("📷 Take a Picture", "🌇 Choose a image")
while True:
    s = droid.menu("AI Super Resolution", menu, None)
    picName = time.strftime("%Y%m%d_%H%I%S")+".jpg"
    if s is not None:
        if s == 0:
            img = droid.camera("/storage/extSdCard/DCIM/Camera/"+picName)
            if img:
                torch.gen(img, True)
            else:
                droid.alert("AI Super Resolution", "Camera Error!")
        else:
            file = droid.pick('image/*')
            if file:
                torch.gen(file['_data'])
            else:
                droid.alert("AI Super Resolution", "no file selected!")
    else:
        droid.alert("AI Super Resolution", "no menu selected!")
        break
