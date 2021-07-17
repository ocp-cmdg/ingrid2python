
[Ingrid on kage](http://kage.ldeo.columbia.edu:81/expert):

```
%ingrid:
/ds {(/DC/sst.mon.mean.nc) readCDF} def
ds
```

[Python in Jupyter Notebook]()

```
#python:
import xarray as xr
import os
os.system('wget ftp://ftp.cdc.noaa.gov/Datasets/COBE/sst.mon.mean.nc')
ds = xr.open_dataset('sst.mon.mean.nc')
ds
```

