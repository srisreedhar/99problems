# sri sreedhar
# get_weather_info.py
# pulls data from openweathermap.org
# responce is in JSON format,
# urllib2 | requests .


def get_weather_info(PLACE=Hyderabad,APIKEY):
	  #http://api.openweathermap.org/data/2.5/weather?q=hyderabad&appid=APIKEY_HERE
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s"%(PLACE,APIKEY)
    response = urllib2.urlopen(url).read()
    return response