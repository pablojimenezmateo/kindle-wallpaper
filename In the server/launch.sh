#!/bin/sh

cd "$(dirname "$0")"

python3 programs/parse_weather.py
python3 programs/parse_ical.py

rsvg-convert --background-color=white -o almost_done.png almost_done.svg

#We optimize the image
pngcrush -c 0 -ow almost_done.png done.png

#We move the image where it needs to be
rm /var/www/kindle/done.png
mv done.png /var/www/kindle/done.png

rm basic.ics
rm after-weather.svg
rm almost_done.png
rm almost_done.svg

