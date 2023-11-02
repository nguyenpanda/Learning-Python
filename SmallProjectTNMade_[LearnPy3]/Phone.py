import phonenumbers
import folium
import opencage
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

number = '+84'
# 0789978919
p_number = phonenumbers.parse(number)
location = geocoder.description_for_number(p_number, 'en')
print(location)

service_provider = carrier.name_for_number(p_number, 'en')
print(service_provider)

key = 'b545e818e30d4a53b6464377ba62d10b'
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat)
print(lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save('phone.html')
print("phone location generated!")
