import requests
from qpycmd import droid
import os

key = ''

def gen(file, rep=False):
	droid.sprogress_show('AI Super Resolution', 'processing %s ..'%file)
	myfile = os.path.basename(file)
	folder = os.path.dirname(file)
	r = requests.post("https://api.deepai.org/api/torch-srgan",files={'image': open(file, 'rb'),}, headers={'api-key': key})
	js = r.json()
	if 'output_url' in js:
		c = requests.get(js['output_url'], verify=False)
		if rep:
			sav = file
		else:
			sav = folder+'/'+'SR_'+myfile
		with open(sav, 'wb') as f:
			f.write(c.content)
		droid.sprogress_hide()
		a = droid.alert('AI Super Resolution', 'success, saved photo at '+sav, button=('close','view'))
		if a == 'view':
			droid.view(sav)