import numpy as np
import matplotlib.pyplot as plt
from time import time
from netCDF4 import Dataset
from datetime import date
from datetime import datetime

now = int(datetime.now().strftime("%H"))//6*6
start = time()
RES = str('0p25') #1p00, 0p50, 0p25
YYYYMMDD = str(date.today().strftime("%Y%m%d"))
HH = str(now) if now >=12 else f"0{str(now)}"
print(YYYYMMDD, HH, RES)

url = 'https://nomads.ncep.noaa.gov/dods/gfs_{0}/gfs{1}/gfs_{0}_{2}z'.format(RES, YYYYMMDD, HH)
ds = Dataset(url)
lon1 = float(ds.variables['lon'][0])
lon2 = float(ds.variables['lon'][-1])
lat1 = float(ds.variables['lat'][0])
lat2 = float(ds.variables['lat'][-1])
nx = ds.dimensions['lon'].size
ny = ds.dimensions['lat'].size
dx = (lon2 - lon1 + 1) / nx
dy = (lat2 - lat1 + 1) / ny
fcTime = 0

if lat1 < lat2:
    ugrd10m = np.flipud(ds.variables['ugrd10m'][fcTime,:,:]).flatten().filled().tolist()
    vgrd10m = np.flipud(ds.variables['vgrd10m'][fcTime,:,:]).flatten().filled().tolist()
    tmp = lat2
    lat2 = lat1
    lat1 = tmp
    dy = abs(dy)  # negative dy breaks wind-layer
else:
    ugrd10m = ds.variables['ugrd10m'][fcTime,:,:].flatten().filled().tolist()
    vgrd10m = ds.variables['vgrd10m'][fcTime,:,:].flatten().filled().tolist()

lo1 = int(lon1)
la1 = int(lat1)
lo2 = int(lon2)
la2 = int(lat2)

uComp = np.array(ugrd10m)
vComp = np.array(vgrd10m)
M = np.sqrt(uComp*uComp+vComp*vComp) #magnitude of vector
Angle = np.arctan2(-uComp,-vComp) * 180 / np.pi #calculate angle of vector. (-uComp,-vComp) 0deg = north to south, 90deg = east to west. (vComp,uComp) 0deg = west to east, 90deg = south to north.
for i, angle in enumerate(Angle):
     Angle[i] = angle if angle>=0 else angle+360
longCord, latCord = np.meshgrid(np.linspace(lo1,lo2,nx),np.linspace(la1,la2,ny))

header = {
    "RES":RES,
    "YYYYMMDD":YYYYMMDD,
    "HH":HH,
    "lo1":lo1,
    "lo2":lo2,
    "la1":la1,
    "la2":la2,
    "nlo":nx,
    "nla":ny,
    "dlo":dx,
    "dla":dy,
}
data = {
    "ugrd10m":ugrd10m,
    "vgrd10m":vgrd10m,
    "M":M,
    "Angle":Angle
}

end = time()
print('Duration:',end-start)
qq=plt.quiver(longCord, latCord, uComp, vComp, M, cmap=plt.cm.viridis)
plt.colorbar(qq, cmap=plt.cm.viridis)
plt.title("World Wind Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
