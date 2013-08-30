import urllib2
from xml.dom import minidom
import datetime
import codecs


#Code of my city, if you don't know what to do here, read the README
CODE = ""
weather_xml = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=' + CODE + '&u=c').read()
dom = minidom.parseString(weather_xml)

#Get weather Tags
xml_temperatures = dom.getElementsByTagName('yweather:forecast')

#Get today Tag
today = xml_temperatures[0]

#Get info
low = today.getAttribute('low')
high = today.getAttribute('high')
image = today.getAttribute('code')
date = today.getAttribute('date')
image_url = 'icons/' + image + '.svg'

# Open SVG to process
output = codecs.open('icons/template.svg', 'r', encoding='utf-8').read()


#Read icon (Just the path line)
f = codecs.open(image_url ,'r', encoding='utf-8')
f.readline()
icon = f.readline()
f.close()

# Insert icons and temperatures
output = output.replace('TODAY',date)
output = output.replace('ICON_ONE',icon)
output = output.replace('HIGH_ONE',high)
output = output.replace('LOW_ONE',low)

# Write output
codecs.open('after-weather.svg', 'w', encoding='utf-8').write(output)
