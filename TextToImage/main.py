# -*-coding:utf8;-*-
import requests
from qpycmd import droid, path
import os
import time

key = ''
os.chdir(path)
file = time.strftime("%Y%m%d_%H%I%S")+".jpg"
text = droid.input("Text 2 Image Generator", "please enter text bellow")
if not text:
    quit("input text failed!")
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': text,
    },
    headers={'api-key': key}
)
js = r.json()
if "output_url" in js:
    req = requests.get(js['output_url'])
    with open('output/'+file, 'wb') as f:
        f.write(req.content)
    a = droid.alert('Text 2 Image Generator', "success, saved to %s" %
                    path+'/output/'+file, button=("close", "view"))
    if a == "view":
        droid.view(path+'/output/'+file)
else:
    droid.warn("ERROR", r.text)
