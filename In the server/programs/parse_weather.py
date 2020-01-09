import time, uuid, urllib, urllib2
from xml.dom import minidom
import datetime
import hmac, hashlib
import codecs
from base64 import b64encode

#Weather API Python sample code from Yahoo
#Copyright 2019 Oath Inc. Licensed under the terms of the zLib license see https://opensource.org/licenses/Zlib for terms.

#Basic info (You need your own credentials from https://developer.yahoo.com/weather/)
url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
app_id = 'abc1234567'
consumer_key = 'qwerty1234567890qwerty'
consumer_secret = '12345qwerty4567890'
concat = '&'
query = {'location': 'berlin,de', 'format': 'xml', 'u': 'c'}
oauth = {
'oauth_consumer_key': consumer_key,
'oauth_nonce': uuid.uuid4().hex,
'oauth_signature_method': 'HMAC-SHA1',
'oauth_timestamp': str(int(time.time())),
'oauth_version': '1.0'
}

#Prepare signature string (merge all params and SORT them)
merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + '=' + urllib.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base_str = method + concat + urllib.quote(url, safe='') + concat + urllib.quote(concat.join(sorted_params), safe='')

#Generate signature
composite_key = urllib.quote(consumer_secret, safe='') + concat
oauth_signature = b64encode(hmac.new(composite_key, signature_base_str, hashlib.sha1).digest())

#Prepare Authorization header
oauth['oauth_signature'] = oauth_signature
auth_header = 'OAuth ' + ', '.join(['{}="{}"'.format(k,v) for k,v in oauth.iteritems()])

#Send request
url = url + '?' + urllib.urlencode(query)
request = urllib2.Request(url)
request.add_header('Authorization', auth_header)
request.add_header('X-Yahoo-App-Id', app_id)
weather_xml = urllib2.urlopen(request).read()
#debug: print(weather_xml)

#Feeding yahoo weather data into DOM
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

#Open SVG to process
output = codecs.open('icons/template.svg', 'r', encoding='utf-8').read()

#Read icon (Just the path line)
f = codecs.open(image_url ,'r', encoding='utf-8')
f.readline()
icon = f.readline()
f.close()

#Insert icons and temperatures
output = output.replace('TODAY',date)
output = output.replace('ICON_ONE',icon)
output = output.replace('HIGH_ONE',high)
output = output.replace('LOW_ONE',low)

#Write output
codecs.open('after-weather.svg', 'w', encoding='utf-8').write(output)
