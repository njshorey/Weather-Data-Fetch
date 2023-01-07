import math

def deg2rad(deg):
  return deg * (math.pi/180)

def haversine(lat1,lon1,lat2,lon2):
    R = 6371; # Radius of the earth in km
    p = 0.017453292519943295 #math.pi/180
    c = math.cos
    a = 0.5 - c((lat2 - lat1) * p)/2 + c(lat1 * p) * c(lat2 * p) * (1 - c((lon2 - lon1) * p))/2
    return R*2 * math.asin(math.sqrt(a))

lat1 = 50
lat2 = -75
lon1 = 0
lon2 = 180
j = haversine(lat1,lon1,lat2,lon2)
print(j)