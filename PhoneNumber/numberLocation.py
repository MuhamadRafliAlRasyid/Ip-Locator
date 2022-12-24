import  phonenumbers

import folium

from myNumber import number

from  phonenumbers import geocoder

Key = 'a16645552d424ce3b5c92179f0c8e26e'

samNumber = phonenumbers.parse(number)

yourLocaton = geocoder.description_for_number(samNumber, "en")
print(yourLocaton)

## get provider number

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocaton)

results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start =9)

folium.Marker([lat, lng],popup=yourLocaton).add_to(myMap)

## save file in html file

myMap.save("mylocation.html")



