import geoip2.database

reader = geoip2.database.Reader('GeoLite2-City_20190326/GeoLite2-City.mmdb')


response = reader.city('201.6.197.29')


print(response.country.iso_code)
print(response.country.name)
print(response.subdivisions.most_specific.name) #good
print(response.city.name) #good com acento
print(response.location.latitude)
print(response.location.longitude)

reader.close()




