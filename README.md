Kindle weather and calendar displayer
====================================

Author: Pablo Jiménez Mateo

Do you use a Kindle and hope that the wallpapers could be more useful? Well, that has just changed,
with this program you will display the weather and some task to do retrieved from Yahoo Weather
and Google calendar!

You can see a preview in the preview.png file

Based on the idea of Matthew Petroff: http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

Dependencies
------------

You should have previously Jailbreaked you kindle (http://www.shatteredhaven.com/2012/11/1337365-ssh-on-kindle-4-usbnetwork-hack.html)
and enabled the "screensavers" folder (http://www.gadget-reviews.me/2012/02/how-to-custom-screensavers-on-amazon.html)

- https://github.com/collective/icalendar
- librsvg2-bin 
- pngcrush

Setup
-------------

** programs/parse_ical **

To get your .ical for parse_ical go to https://support.google.com/calendar/answer/37103?hl=en and follow the instructions

** programs/parse_weather **

To get your city code for parse_weather go to http://weather.yahoo.com/, search your city and get the last numbers.

As an example my city code would be 756804

http://weather.yahoo.com/spain/valencia/castello-de-la-plana-756804/

This program is licensed under Creative commons Attribution 3.0 Unported, more info : 
http://creativecommons.org/licenses/by/3.0/deed.en_US
