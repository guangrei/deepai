# -*-coding:utf8;-*-
from qpycmd import path, droid
import os
import requests

key = ''
os.chdir(path)
droid.edit(path+'/input.txt')
r = requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    files={
        'text': open('input.txt', 'rb'),
    },
    headers={'api-key': key}
)
js = r.json()
if 'output' in js:
    droid.alert('Sentiment Analysis', '\n'.join(js['output']))
else:
    droid.warn("ERROR", r.text)
