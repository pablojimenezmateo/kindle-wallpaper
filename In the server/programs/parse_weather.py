import urllib.request, json 
from datetime import date
import codecs

# API key, don't abuse it or get your on in https://openweathermap.org
API_KEY = "3d17566eeb85d89b6782df5f81b420d7"

# Code of your city, if you don't know what to do here, read the README
CODE = ""

# Read the JSON
with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=" + CODE + "&appid=" + API_KEY + "&units=metric") as url:
    data = json.loads(url.read().decode())

# Get API info
low   = data["main"]["temp_min"]
high  = data["main"]["temp_max"]
image = data["weather"][0]["id"]

# This tells if it is night "n" or day "d"
light = data["weather"][0]["icon"][-1:]

# Extra info
date = date.today().strftime("%d %b %Y")

# Get the correct icon
image_path = 'icons/' + str(image) + light + '.svg'

# Open SVG to process
output = codecs.open('icons/template.svg', 'r', encoding='utf-8').read()

# Read icon (Just the path line)
f = codecs.open(image_path ,'r', encoding='utf-8')
f.readline()
icon = f.readline()
f.close()

# Insert icons and temperatures
output = output.replace('TODAY',date)
output = output.replace('ICON_ONE', icon)
output = output.replace('HIGH_ONE',"{:2.1f}".format(high))
output = output.replace('LOW_ONE',"{:2.1f}".format(low))

# Write output
codecs.open('after-weather.svg', 'w', encoding='utf-8').write(output)
