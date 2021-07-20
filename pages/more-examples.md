---
title: Ingrid2Python
---

## Advanced Examples

<details> <summary><b>EOFs/PCs </b></summary> <p>  
Find the 3 leading EOFs and PCs. Note that ingrid and `eofs.xarray` use different scalings.

```
%ingrid:
ds .sst {Y cosd}[lon lat][time]svd ev 1 3 RANGE
```

```
#python:
from eofs.xarray import Eof  # see [documentation](https://ajdawson.github.io/eofs/latest/api/eofs.xarray.html)
ds_anom = ds.groupby('time.month') - ds.groupby('time.month').mean()
solver = Eof(ds_anom.sst)
pcs = solver.pcs(npcs=3)
eofs = solver.eofsAsCorrelation(neofs=3)
```
</p> </details>

<details> <summary><b>Find the depth of the 20 degree isotherm</b></summary> <p>  

```
$ingrid on kage
/ds {SOURCES .LOCAL .ORAs5_thetao-clim.nc deptht 0 500 RANGE lat -30 30 RANGE [time]average} def

ds .thetao
deptht exch [20]deptht toS
```
  
```
#python
import xarray as xr
import xgcm.  # need version >= 0.5.2
import numpy as np

url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.ORAs5_thetao-clim.nc/.thetao/dods'
ds = xr.open_dataset(url,decode_times=False).sel(deptht=slice(0,500),lat=slice(-30,30)).mean('time')

depth_3d = ds.deptht.broadcast_like(ds.thetao)
grid = xgcm.Grid(ds,periodic=False)
h20 = grid.transform(depth_3d, 'Z', np.array([20]), target_data=ds.thetao, method='linear')
```
</p> </details> 
