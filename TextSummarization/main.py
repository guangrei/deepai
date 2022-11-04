# -*-coding:utf8;-*-
from qpycmd import path, droid
import os
import requests

key = ''
os.chdir(path)
droid.edit(path+'/input.txt')
r = requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text': open('input.txt', 'rb'),
    },
    headers={'api-key': key}
)
js = r.json()
if 'output' in js:
    droid.warn("Text Summarization", js['output'])
    with open('output.txt', 'w') as f:
        f.write(js['output'])
else:
    droid.warn("ERROR", r.text)
