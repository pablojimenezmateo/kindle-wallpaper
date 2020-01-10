from icalendar import Calendar
import datetime
from datetime import timedelta
import urllib.request
import time
import codecs

#Your private ical URL, if you don't know what to do here, read the README
ICAL_URL = ""

urllib.request.urlretrieve(ICAL_URL, "basic.ics")

cal = Calendar.from_ical(open('basic.ics','rb').read())

all_day_events = []
normal_events = []

for component in cal.walk('vevent'):

    #Because of timezone
    delta = timedelta(hours = 3)

    date_start = component['DTSTART'].dt + delta

    #Check if it is today
    if( date_start.timetuple().tm_yday == datetime.datetime. now().timetuple().tm_yday ):
        if date_start.timetuple().tm_year == datetime.datetime.now().timetuple().tm_year:

            #Check if is not  all day (It does have time so datetime works)
            if ( type(date_start) is datetime.datetime ):
                
                normal_events.append(component)
            else:
                all_day_events.append(component)

#Sort by date
normal_events.sort(key=lambda hour: hour['DTSTART'].dt)

# Finnish svg
output = codecs.open('after-weather.svg', 'r', encoding='utf-8').read()

count = 0

for event in normal_events:

    date_start = event['DTSTART'].dt + delta

    date_end = event['DTEND'].dt + delta

    entry_date = date_start.strftime("%H:%M") + '-' +  date_end.strftime("%H:%M") 
    entry_name = event['SUMMARY'] 


    output = output.replace('hour'+ str(count) ,entry_date)
    output = output.replace('Name' + str(count) ,entry_name)

    count+=1
    #Just 5 tasks a day keeps the doctor away
    if (count == 5):

        break

count = 0

for event in all_day_events:

    entry_name = event['SUMMARY']

    output = output.replace('AllDay' + str(count) , entry_name)

    if (count == 2 ):
        
        break

#Erase unsused marks
output = output.replace('hour0' ,'')
output = output.replace('hour1' ,'')
output = output.replace('hour2' ,'')
output = output.replace('hour3' ,'')
output = output.replace('hour4' ,'')

output = output.replace('Name0' ,'')
output = output.replace('Name1' ,'')
output = output.replace('Name2' ,'')
output = output.replace('Name3' ,'')
output = output.replace('Name4' ,'')

output = output.replace('AllDay0' ,'')
output = output.replace('AllDay1' ,'')



# Write output
codecs.open('almost_done.svg', 'w', encoding='utf-8').write(output)















