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

**In the Kindle**

- Move the file kindle/launch.sh to /mnt/us/launch.sh and add rights

    scp launch.sh root@192.168.15.244:/mnt/us/

    chmod 755 /mnt/us/launch.sh

- Mount the partition in Read/Write

    mntroot rw

- Edit the crontab file and append your job
 
    vi /etc/crontab/root 
    50 6 * * * /mnt/us/launch.sh

**programs/parse_ical**

You need to open the file programs/parse_ical and put your .ical URL in the variable ICAL_URL

To get your .ical for parse_ical go to https://support.google.com/calendar/answer/37103?hl=en and follow the instructions

**programs/parse_weather**

You need to open the file programs/parse_weather and put your city code in the variable CODE

To get your city code for parse_weather go to http://weather.yahoo.com/, search your city and get the last numbers.

As an example my city code would be 756804

http://weather.yahoo.com/spain/valencia/castello-de-la-plana-756804/

This program is licensed under Creative commons Attribution 3.0 Unported, more info : 
http://creativecommons.org/licenses/by/3.0/deed.en_US
