#-*-coding:utf8;-*-
from qpycmd import droid
import requests

key = ''
text = droid.input("Text Generation", "please enter the prompt bellow")
if text:
	r = requests.post(
	    "https://api.deepai.org/api/text-generator",
	    data={
	        'text': text,
	    },
	    headers={'api-key': key}
	)
	js = r.json()
	if 'output' in js:
		droid.warn("Text Generation", js['output'])
	else:
		droid.warn('ERRROR', r.text)