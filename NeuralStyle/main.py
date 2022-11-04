from qpycmd import droid
import requests
import os

key = ''
droid.alert("Style Transfer","1.Select a styled image")
style = droid.pick('image/*')
if style:
	style = style['_data']
else:
	quit("operation 1 failed!")
droid.alert("Style Transfer","1.Select a image for styling")
content = droid.pick('image/*')
if content:
	content = content['_data']
else:
	quit("operation 2 failed!")
folder = os.path.dirname(content)
file = "styled_"+os.path.basename(content)
r = requests.post(
    "https://api.deepai.org/api/neural-style",
    files={
        'style': open(style, 'rb'),
        'content': open(content, 'rb'),
    },
    headers={'api-key': key}
)
js = r.json()
if "output_url" in js:
	req = requests.get(js['output_url'])
	with open(folder+'/'+file, 'wb') as f:
		f.write(req.content)
	a = droid.alert('Style Transfer', "success, saved to %s"%folder+'/'+file, button=("close", "view"))
	if a == "view":
		droid.view(folder+'/'+file)
else:
	droid.warn("Debug", r.text)