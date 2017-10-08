import os
import json
import ctypes
import urllib
import urllib2
import os.path

api_key = "" # get your api key from https://unsplash.com/developers
url = "https://api.unsplash.com/photos/random?client_id=" + api_key

user_path = os.environ["USERPROFILE"]
pictures_path = "Pictures"
refreshr_path = "Refreshr"
photo_name = "background.jpeg"

working_path = os.path.join(user_path, pictures_path, refreshr_path)

wallpaper = os.path.join(working_path, photo_name)
wallpaper = wallpaper.replace("\\", "/")

if not os.path.exists(working_path):
    os.makedirs(working_path)

try:
    print "Downloading image."
    link = urllib2.urlopen(url)
    string = link.read()
    link.close()
    json = json.loads(string)
    photo = json["urls"]["full"]
    urllib.urlretrieve(photo, wallpaper)
    print "Done."
    print "Setting wallpaper."
    ctypes.windll.user32.SystemParametersInfoA(20, 0, wallpaper, 0)
    print "Done."

except Exception:
    pass
