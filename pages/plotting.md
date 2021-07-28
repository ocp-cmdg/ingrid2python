---
title: Ingrid2Python
---

## Plotting Examples

<details> <summary><b>Projections/Transforms/Features</b></summary> <p>  

```
import xarray as xr
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature
```
  
```
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.sst.mon.mean.nc/.sst/time/AVERAGE/dods'
ds = xr.open_dataset(url).sst
```
  
Set a plot size and pick a [cartopy projection](https://scitools.org.uk/cartopy/docs/latest/crs/projections.html)
  
```
fig = plt.figure(figsize=(9, 5))

# Pick a [cartopy projection](https://scitools.org.uk/cartopy/docs/latest/crs/projections.html)
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180));
```
Plot coastlines and then pick a [transform](https://scitools.org.uk/cartopy/docs/latest/tutorials/understanding_transform.html).
  
```
ax.coastlines()
ds.plot.contour(ax=ax, transform=ccrs.PlateCarree(),levels=30)
```
Add [feature](https://scitools.org.uk/cartopy/docs/latest/matplotlib/feature_interface.html), if desired:  (typing \<Tab\> after `cfeature.` will list possible completions)
  
```
ax.add_feature(cfeature.BORDERS)
```
<p align="center"><img src="../assets/imgs/basic-cartopy.png"></p>
</p> </details>


<details> <summary><b>More Features, Labels</b></summary> <p>  

```
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
```
  
```
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.sst.mon.mean.nc/.sst/time/AVERAGE/dods'
ds = xr.open_dataset(url).sel(lat=slice(50,-50)).sst
```
  
```
fig = plt.figure(figsize=(8,5))
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
ax.set_extent([100, 290, -50, 50], crs=ccrs.PlateCarree())

# Put a background image on for nice sea rendering.
ax.stock_img()
CS = ds.plot.contour(ax=ax, transform=ccrs.PlateCarree(),colors='k',vmin=10,vmax=30,levels=11)
# Add labels on contours
ax.clabel(CS, inline=1, fontsize=8, fmt='%1.0f')

# Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
states_provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='50m',
    facecolor='none')

ax.add_feature(cfeature.COASTLINE,zorder=3)
ax.add_feature(cfeature.BORDERS, edgecolor='gray')
ax.add_feature(states_provinces, edgecolor='gray')

# Add longitude, latitude labels
gl = ax.gridlines(draw_labels=True, alpha=0.0, xlocs=np.arange(-160,181,20))
gl.top_labels = False
```
<p align="center"><img src="../assets/imgs/more-cartopy.png"></p>
</p> </details>

<details> <summary><b>Subplots</b></summary> <p>  

The built-in xarray plotting allows for multiple plots:
  
```
ds = xr.open_dataset('http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.sst.mon.mean.nc/.sst/dods')
ds_mon_anom = ds.groupby('time.month').mean() - ds.mean('time')
ds_mon_anom.sst.plot(x='lon',y='lat',col='month',col_wrap=4,add_colorbar=0);
```
<p align="center"><img src="../assets/imgs/xarray-subplots.png"></p>
  
But much more control is possible when using `matplotlib` directly, see [subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html).
</p> </details>

<details> <summary><b>Reversing Grid Direction</b></summary> <p>  

The keyword arguments `xincrease` and `yincrease` control the axis direction. 
   
```
import xarray as xr
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.ORAs5_thetao-clim.nc/.thetao/dods'
ds = xr.open_dataset(url,decode_times=False).sel(deptht=slice(0,300),lat=slice(-30,30),lon=slice(150,250)).mean('time')

ds.thetao.sel(lat=slice(-2,2)).mean('lat').plot.contourf(vmin=10,vmax=30,levels=11,yincrease=False)
```
<p align="center"><img src="../assets/imgs/theta.png"></p>
  
</p> </details>
<details> <summary><b>Types of Plots</b></summary> <p>  

Plotting DataArrays: For examples of all of the following, see [xarray plotting](http://xarray.pydata.org/en/stable/user-guide/plotting.html)
  
- da.plot.pcolormesh()
- da.plot.contour()
- da.plot.contourf()
- da.plot.imshow()
- da.plot.line()
- da.plot.hist()
- da.plot.bar()
- da.plot.step()
- da.plot.surface()
- ds.plot.scatter()
- ds.plot.quiver()
- ds.plot.streamplot()
  
There are also other plotting methods, such as ds.plot.violin, ds.plot.bivariate, ds.plot.table, etc.
  
IRIDL has started using [hvplot](https://hvplot.holoviz.org/), which is an interactive plotting tool. We have installed it on `carney`, and find it cute, but somewhat frustrating.
  
</p> </details>

<details> <summary><b>Overlay Contours on Colors</b></summary> <p>  

```
%ingrid
 SOURCES .DASILVA .SMD94 .anomalies .sst correlationcolorscale
  DATA -2 2 RANGE
  X -100 20 RANGE
  Y 0 90 RANGE
  /color_smoothing null def
 SOURCES .DASILVA .SMD94 .anomalies .slp
   X -100 20 RANGE
   Y 0 90 RANGE
   DATA 5 STEP
   X Y fig: colors contours land :fig
```
  <p align="center"><img src="../assets/imgs/color-contour-ingrid.png" width="80%"></p>
  
Try to match this ingrid figure as closely as possible in python ...
  
```
#python
import xarray as xr
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import colors

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
```
  
```
# Get the Dataset
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.DASILVA/.SMD94/.anomalies/.sst/dods'
url2 = 'http://kage.ldeo.columbia.edu:81/SOURCES/.DASILVA/.SMD94/.anomalies/.slp/dods'

ds = xr.open_dataset(url,decode_times=False)
ds['slp'] = xr.open_dataset(url2,decode_times=False).slp

# Fix the grids
ds['T'] = pd.date_range('1945-01',periods=len(ds.T), freq='MS').shift(15,freq='D')
ds.coords['X'] = (ds.coords['X'] + 180) % 360 - 180
ds = ds.sortby(ds.X)

# Restrict the domain
dss = ds.sel(X=slice(-100,20),Y=slice(-10,90)).isel(T=0)
  
## Now make the figure
 
cmap_data = [(0, 'navy'),(0.1, 'blue'),(0.2, 'DeepSkyBlue'),(0.3, 'aquamarine'),(0.4,'PaleGreen'),(0.45,'moccasin'),
             (0.55,'moccasin'),(.6,'yellow'),(.7,'DarkOrange'),(.8,'red'),(1.0,'DarkRed')]
cmap = colors.LinearSegmentedColormap.from_list('correlationcolorscale', cmap_data)
plt.register_cmap('correlationcolorscale', cmap)

fig = plt.figure(figsize=(8,8))

ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0))
ax.set_extent([-100, 20, 0, 90], crs=ccrs.PlateCarree())

cb = dss.sst.plot.contourf(ax=ax, transform=ccrs.PlateCarree(), vmin=-2, vmax=2, levels=41, cmap='correlationcolorscale',
                           add_colorbar=False,rasterized=True)
CS = dss.slp.plot.contour(ax=ax, colors = 'black', transform=ccrs.PlateCarree(), vmin=-20, vmax=20, levels=9)
CS.collections[4].set_linewidth(3) # make the zero line wider
ax.clabel(CS, inline=1, fontsize=8, fmt='%1.0f')

ax.add_feature(cfeature.LAND,facecolor='k')

cbar = plt.colorbar(cb, extend = 'min', shrink=1.0, pad=.10, label=r'SSTA ($\degree C$)', orientation='horizontal')

xticks = np.arange(-80, 0.1, 20)
yticks = np.arange(20, 80.1, 20)
ax.set_xticks(xticks, crs=ccrs.PlateCarree())
ax.set_yticks(yticks, crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=True))
ax.yaxis.set_major_formatter(LatitudeFormatter())

ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
```
  <p align="center"><img src="../assets/imgs/color-contour-correlation.png" width="80%"></p>
</p> </details>

<details> <summary><b>Plot global SST centered at a given longitude</b></summary> <p>  

```
#python
import pandas as pd
import xarray as xr
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
import cartopy
from cartopy.util import add_cyclic_point
import cartopy.crs as ccrs
from cartopy.mpl.geoaxes import GeoAxes
from mpl_toolkits.axes_grid1 import AxesGrid
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# Get the Dataset
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.DASILVA/.SMD94/.anomalies/.sst/dods'

ds = xr.open_dataset(url,decode_times=False)
# Fix the grids
ds['T'] = pd.date_range('1945-01',periods=len(ds.T), freq='MS').shift(15,freq='D')

#for center the plot to 60 (or any longitude)
center_lon = 60
ds_60W180E = ds.copy()
ds_60W180E.coords['X'] = (ds_60W180E.coords['X']+180)%360 - center_lon
ds_60W180E = ds_60W180E.sortby(ds_60W180E.X)

# Prepare the figure
fig = plt.figure(1,(8,8))
projection = ccrs.PlateCarree(central_longitude=center_lon)
axes_class = (GeoAxes,
                  dict(map_projection=projection))
axgr = AxesGrid(fig,111, axes_class=axes_class,
    nrows_ncols=(1, 1),
    axes_pad=0.6,
    cbar_location='right',
    cbar_mode='single',
    cbar_pad=0.2,
    cbar_size='3%',
    label_mode='')  # note the empty label_mode    

levels = np.arange(-4,4.2,0.2)
for i, ax in enumerate(axgr):
    data, lon = add_cyclic_point(ds.sst[0,:,:].values, coord=ds.X)
    dumy, lon_60W180E = add_cyclic_point(ds_60W180E.sst.values, coord=ds_60W180E.X) # X=-180:180
    ax.coastlines()
    ax.set_xticks(np.linspace(-180,180, 10), crs=projection)
    ax.set_yticks(np.linspace(-70,70, 15), crs=projection)
    title = 'SST for ' + np.datetime_as_string(ds['T'][0].values, unit='M')
    
    ax.set_title(title,y=1.02)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-.', linewidth=1,edgecolor='k')
    p = ax.contourf(lon_60W180E, ds_60W180E.Y, data,levels,\
                    transform=projection,\
                    cmap='RdBu_r')

ax.set_xlim([-180,180]) 
ax.set_ylim([-70,75]) 
cbar = axgr.cbar_axes[0].colorbar(p)
cbar.ax.set_ylabel('SST ($^\circ$C)', rotation=90,fontsize=14)

plt.show()
```
</p> </details>

<p align="center"><img src="../assets/imgs/SST_hb.png" width="80%"></p>
