Kindle weather and calendar displayer
====================================

Author: Pablo Jiménez Mateo

![ScreenShot](https://raw.github.com/gef3233/kindle-wallpaper/master/with_kindle.JPG)

Do you use a Kindle and hope that the wallpapers could be more useful? Well, that has just changed,
with this program you will display the weather and some task to do retrieved from Yahoo Weather
and Google calendar!

You can see a preview in the preview.png file

Based on the idea of Matthew Petroff: http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

Dependencies
------------

Note that you need a server for this, a Raspberry Pi is more than enough

You should have previously Jailbreaked you kindle (http://www.shatteredhaven.com/2012/11/1337365-ssh-on-kindle-4-usbnetwork-hack.html)
and enabled the "screensavers" folder (https://wiki.mobileread.com/wiki/Kindle_Screen_Saver_Hack_for_all_2.x,_3.x_%26_4.x_Kindles)

- https://github.com/collective/icalendar
- librsvg2-bin 
- pngcrush

Setup
-------------

### In the Kindle

- Move the file kindle/launch.sh to /mnt/us/launch.sh and add rights
```bash
    scp launch.sh root@192.168.15.244:/mnt/us/

    chmod 755 /mnt/us/launch.sh
```
- Mount the partition in Read/Write
```bash
    mntroot rw
```
- Edit the crontab file and append your job
```bash
    vi /etc/crontab/root 
    50 6 * * * /mnt/us/launch.sh
```

### In the server

You must edit the following files:

**programs/parse_ical**

You need to open the file programs/parse_ical and put your .ical URL in the variable ICAL_URL

To get your .ical for parse_ical go to https://support.google.com/calendar/answer/37103?hl=en and follow the instructions

**programs/parse_weather**

You need to open the file programs/parse_weather and put your city code in the variable CODE

To get your city code for parse_weather download http://bulk.openweathermap.org/sample/city.list.json.gz, search your city id.

As an example my city code would be 6356995

```
  {
    "id": 6356995,
    "name": "Castellón de la Plana/Castelló de la Plana",
    "country": "ES",
    "coord": {
      "lon": -0.05768,
      "lat": 39.992901
    }
```

**launch.sh**

You may need to change your path if you are not using the default yourserver/kindle structure.

**General configuration**

Finally you should create a folder in your webserver readable by your kindle when trying to download it (In this example would be yourserver/kindle):

```bash
    sudo mkdir /var/www/kindle
    sudo chown www-data:www-data /var/www/kindle
    sudo chmod 755 /var/www/kindle
```

Give the script launch permissions:

```bash
    chmod 755 launch.sh
```

Append the cronjob some minutes before the one in the Kindle:

```bash
    crontab -e 
    30 6 * * * /path/to/launch.sh
```

#### Special thanks

kevinabraun@gmail.com for the remaining weather icons.

This program is licensed under Creative commons Attribution 3.0 Unported, more info : 
http://creativecommons.org/licenses/by/3.0/deed.en_US
