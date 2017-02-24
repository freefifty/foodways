import os, csv, re
import requests
from geopy.geocoders import Nominatim

# using geopy library
def get_lat_lon_geopy(address):
  geolocator = Nominatim()
  try:
    location = geolocator.geocode(address)
    return location.latitude, location.longitude
  except:
  	print("Can't find the coordinates for", address)
  	return 0,0
  	# new_address = address.split(",")[0] + ", Lisbon, Portugal"
  	# try:
  	# 	location = geolocator.geocode(address)
  	# 	return location.latitude, location.longitude
  	# except:
  	# 	print("Can't find the coordinates for", address)
  	# 	return 0,0

# geo tag locals listed in a csv file

# Read in raw data from csv
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
file_name = parent_dir + '/data/foodways/happy_cow_listings.csv'
file_name2 = parent_dir + '/data/foodways/happy_cow_coordinate_listings.csv'

csvfile = open(file_name, 'r')
dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=';')
csvfile.seek(0)
data = csv.DictReader(csvfile, dialect=dialect)


with open(file_name2, "w") as ofile:
	# open a csv writer
    writer = csv.writer(ofile, delimiter=';')
    writer.writerow(["name", "address", "phone", "description", "tags", "lat", "long"])

    for row in data:
    	name = row.get('name')
    	address = row.get('address')
    	# process address: remove all text which might be between brakets
    	address = re.sub(r'\([^|)]+\)', '', address)
    	phone = row.get('phone')
    	description = row.get('description')
    	tags = row.get('tags')
    	latitude = 0
    	longitude = 0
    	if address != "address":
    		latitude, longitude = get_lat_lon_geopy(address)
    	if(latitude != 0 and longitude != 0):
    		writer.writerow([name, address, phone, description, tags, latitude, longitude])
    	# writer.writerow([name, address, phone, description, tags, latitutde, longitude])