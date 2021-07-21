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

```
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
```
</p> </details>
