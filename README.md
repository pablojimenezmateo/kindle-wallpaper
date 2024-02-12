Kindle weather and calendar displayer
====================================

Author: Pablo Jiménez Mateo

Addition by luedi0:
Bugfix: All day events trunkated to one
Addition of docker container for (server) wallpaper generation.


![ScreenShot](https://raw.github.com/gef3233/kindle-wallpaper/master/with_kindle.JPG)

Do you use a Kindle and hope that the wallpapers could be more useful? Well, that has just changed,
with this program you will display the weather and some task to do retrieved from Open Weather
and Google calendar!

You can see a preview in the preview.png file

Based on the idea of Matthew Petroff: http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

Prerequisites
------------

- Webserver<br>
You will need a simple (static) webserver with Python 3 installed. An easy way to run this is any Raspberry Pi with a fixed IP.
Alternatively it can be run in any other environment like a Docker container or VM.<br>
https://hub.docker.com/r/luedi0/apache2-python3<br>
This container runs the latest Ubuntu server with Apache 2 httpd and Python 3 as well as the below dependencies.
The script and http directory (webroot) are defined as bind points (pointed to host directory at deployment). The container has unattended security upgrades enabled.

- Amazon Kindle that can be jailbroken


Dependencies
------------

You should have previously Jailbroken your kindle (http://www.shatteredhaven.com/2012/11/1337365-ssh-on-kindle-4-usbnetwork-hack.html)
and enabled the "screensavers" folder (https://wiki.mobileread.com/wiki/Kindle_Screen_Saver_Hack_for_all_2.x,_3.x_%26_4.x_Kindles)

- https://github.com/collective/icalendar
- librsvg2-bin 
- pngcrush

You can install the dependencies with the following 2 commands:

```bash
sudo apt install pngcrush librsvg2-bin python3-pip
python3 -m pip install icalendar

```

Setup
-------------

### In the Kindle

- Move the file kindle/launch.sh to /mnt/us/launch.sh and change its permissions:
```bash
    scp launch.sh root@192.168.15.244:/mnt/us/

    chmod 755 /mnt/us/launch.sh
```
- Mount the partition in Read/Write
```bash
    mntroot rw
```
- Edit the crontab file and append your job (this will make it run everyday at 6:50 AM)
```bash
    vi /etc/crontab/root 
    50 6 * * * /mnt/us/launch.sh
```

### In the server (script directory)

You must edit the following files:

**programs/parse_ical**

You need to open the file programs/parse_ical and put your .ical URL in the variable ICAL_URL

Google calendar<br>
To get your .ical for parse_ical go to https://support.google.com/calendar/answer/37103?hl=en and follow the instructions, you need the URL that is under "Public address in iCal format" and make that calendar public, or the link won't work.

iCloud calendar<br>
The same is also possible with iCloud. Just enable sharing throgh the fan symbol and tick "public" to see the webcal URL. You can either use the easier accessible public URL explained here at apple support https://support.apple.com/en-gb/guide/icloud/mm6b1a9479/icloud or try and get the secret private URL through this tutorial https://www.techrepublic.com/article/how-to-find-your-icloud-calendar-url/
In any case you will need to replace prefix "webcal://" with "https://"

Should you experience a timezone offset when displaying calendar entry times, you will need to adapt the timedelta variable as well. So far, time delta needs to be set to the GMT offset with Google calendar (CET = GMT+1 = 1) and to 0 with iCloud. 

**programs/parse_weather**

You need to open the file programs/parse_weather and put your city code in the variable CODE.

To get your city code for parse_weather download http://bulk.openweathermap.org/sample/city.list.json.gz and search your city id.

As an example my city code would be 6356995:

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

Append the cronjob some minutes before the one in the Kindle (this will execute everydat at 6:30 AM):

```bash
    crontab -e 
    30 6 * * * /path/to/launch.sh
```

#### Special thanks

kevinabraun@gmail.com for the remaining weather icons.

This program is licensed under Creative commons Attribution 3.0 Unported, more info : 
http://creativecommons.org/licenses/by/3.0/deed.en_US
