''' Using https://www.alphavantage.co to retrieve stock prices.  Requires a unique key, freely availalble.
    Sample request: http://api.openweathermap.org/data/2.5/weather?zip=07748,us&units=imperial&APPID=5f0166ed1f0091d6f2aa0b67ebf2514a 

    Sample result:
{"coord":{"lon":-74.12,"lat":40.39},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":32.52,"pressure":1037,"humidity":32,"temp_min":30.92,"temp_max":35.96},"visibility":16093,"wind":{"speed":19.46,"deg":340,"gust":11.3},"clouds":{"all":1},"dt":1549743300,"sys":{"type":1,"id":4686,"message":0.0041,"country":"US","sunrise":1549713393,"sunset":1549751122},"id":420025420,"name":"New Brunswick","cod":200}
'''

import sys
import certifi
import urllib3
import requests



# free api key from https://alphavantage.co
api_key='5f0166ed1f0091d6f2aa0b67ebf2514a'
site_url = 'https://api.openweathermap.org/data/2.5/'

# open config.ini to get symbols to look up
f = open('config.ini', 'r')

# one symbol per line
for zip_code in f:

    # skip empty lines
    if len(zip_code.strip()) == 0:
        continue

    # create the Rest call.  Strip newline from stock_symbol
    zip_code = zip_code.rstrip('\r\n')
    request_url = site_url + 'weather?zip=' + zip_code + ',us&units=imperial&APPID=' + api_key 

    # ignore certificate validation in request (risky for production code)
    urllib3.disable_warnings()

    try:

        response  = requests.get(request_url, verify = False)

    except Exception as e:
        # request failed.  need to log appropriately
        print(str(e))
        sys.exit(1)

    if response.status_code == 200:
        # extract data
        try:
            result = response.json()
            main_data = result['main']
            print('Zipcode: ' + str(zip_code) + ' main data: ' + str(main_data))
        except Exception as e:
            # probably a bad zip_code.  again, logging here
            print(str(e))
        
    else:
        print('request error: ' + str(response.status_code))

