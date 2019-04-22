'''
https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/GHCND/locations/ZIP:70503/data?year=1999&month=12&day=15&token=STKKMBLCoUNqawgRvsloNEQKKdvvSMrh
'''

import requests

#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/GHCND/locations/ZIP:70503/data?year=1999&month=12&day=15'
#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'
uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/FIPS:34'
uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/ZIP:07748'
#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ZIP'
#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=52'
#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locationcategories/'
#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/GHCND?stationid=COOP:310090'
#uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/GHCND?locationid=ZIP:07748'
uri = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01'
header = {'token': 'STKKMBLCoUNqawgRvsloNEQKKdvvSMrh'}
try:
    result = requests.get( uri, headers = header )
except Exception as e:
    print(e)

print( result.status_code )
print( result.json() )
json_result = result.json()
summary = json_result['results']
print(summary)
for attribute in summary:
    print(attribute['datatype'])
    if attribute['datatype'] == 'TMAX':
        max_temp = attribute['value']
    elif attribute['datatype'] == 'TMIN':
        min_temp = attribute['value']

print('max_temp = ' + str(max_temp))
print('min_temp = ' + str(min_temp))
