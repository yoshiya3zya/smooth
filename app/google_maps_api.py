import googlemaps

MAPS_API_KEY = 'AIzaSyDax7Rvk6BJ7Yum-JeFHbY6D5uMJ9c9ymc'

def geocode(address):
   try:
       gmaps = googlemaps.Client(key=MAPS_API_KEY)
       result = gmaps.geocode(address)
       lat = result[0]['geometry']['location']['lat']
       lng = result[0]['geometry']['location']['lng']

       return lat, lng
   except:
       return None, None
