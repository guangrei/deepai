# -*-coding:utf8;-*-
import requests
from qpycmd import droid
import os

key = ''
apiurl = "https://api.deepai.org/api/toonify"
file = droid.pick('image/*')
if file:
    file = file['_data']
    myfile = os.path.basename(file)
    folder = os.path.dirname(file)
    try:
        droid.sprogress_show("Toonify", "processing %s .." % file)
        r = requests.post(apiurl, files={'image': open(file, 'rb'), }, headers={
                          'api-key': key}, verify=False)
        res = r.json()
        droid.sprogress_hide()
    except BaseException as e:
        droid.warn("Error", str(e))
        droid.sprogress_hide()
    if 'output_url' in res:
        c = requests.get(res['output_url'], verify=False)
        with open(folder+"/"+"toonify_"+myfile, "wb") as f:
            f.write(c.content)
        a = droid.alert("Toonify", "success, save toonified image at " +
                        folder+"/"+"toonify_"+myfile, button=("close", "view"))
        if a == "view":
            droid.view(folder+"/"+"toonify_"+myfile)

    else:
        droid.warn("ERROR", r.text)
else:
    droid.alert("ERROR", "no file selected!")
