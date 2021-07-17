## Ingrid to Python/Xarray commands

## Notation

>ds is an ingrid `stream`(or `Field`) or an xarray `dataset` (or `dataarray`)

Try this out [kage](http://kage.ldeo.columbia.edu:81/expert): 
```
%ingrid:
/ds {(/DC/sst.mon.mean.nc) readCDF} def
ds
```

Try this out in a Jupyter Notebook: (type <shift><enter> to see the results)
```
#python:
import xarray as xr
import os
os.system('wget ftp://ftp.cdc.noaa.gov/Datasets/COBE/sst.mon.mean.nc')
ds = xr.open_dataset('sst.mon.mean.nc')
ds
```

<details> <summary>Selecting Data in Datasets </summary> <p>  
A dataset (stream) contains variables, grids, coordinates and metadata. These can be selected by similar methods for ingrid and python. Try selecting `.sst` and `.lon`

```
%ingrid:
ds .sst
```

```
#python:
ds.sst
```
</p> </details>

<details> <summary>Addition/Subtraction/Multiplication </summary> <p>  
In ingrid, compatible objects (streams, numbers) can be added together element by element

```
%ingrid:
ds .sst 273.15 add
```

In python, compatible objects (xarray datasets/dataarrays, numbers) can be added together

```
#python:
ds.sst + 273.15
```
</p> </details>

<details> <summary>Data Selection by grid value </summary> <p>  

```
%ingrid:
ds time (Jan 1960) VALUE lat 20 VALUE
```

```
#python:
ds.sel(time= '1960-01', lat=20, method='nearest')
```
</p> </details>

<details> <summary>Data Selection by grid range </summary> <p>  

```
%ingrid:
ds T (Jan 1982) (Dec 1995) RANGE lon 20 60 RANGE
```

```
#python:
ds.sel(time=slice('1982-01','1995-12'),lon=slice(20,60))
```
</p> </details>

<details> <summary>Averaging over a dimension </summary> <p>  

```
%ingrid:
ds [time] average
ds [lat lon] average
```

```
#python:
ds.mean('time')
ds.mean(['lat','lon'])
```
</p> </details>

<details> <summary>Grid coarsening </summary> <p>  

```
%ingrid:
ds time 12 boxAverage 
```

```
#python:
<ds>.coarsen(time=12,boundary='trim').mean()
```
</p> </details>

<details> <summary>Running Average </summary> <p>  

```
%ingrid:
<ds> time 3 runningAverage
```

```
#python:
<ds>.rolling(time=3, center=True).mean()
```
</p> </details>

<details> <summary>Detrending</summary> <p>  

```
%ingrid:
(ssta.nc)readCDF .ssta [time]detrend-bfl
```

```
#python:
ds = xr.open_dataset('ssta.nc')
dfit = ds.ssta.polyfit('time', 1, skipna=True)
ds.ssta - xr.polyval(coord=ds.time, coeffs=dfit.polyfit_coefficients)
```
</p> </details>

<details> <summary> Find linear trend</summary> <p>  

```
%ingrid:
(ssta.nc)readCDF .ssta dup [time]detrend-bfl sub dup time last VALUE exch T first VALUE sub
```

```
#python:
ds = xr.open_dataset('ssta.nc') 
dfit = ds.ssta.polyfit('time', 1, skipna=True)
ds['linear_fit'] = xr.polyval(coord=ds.time, coeffs=dfit.polyfit_coefficients)
ds['trend'] = (ds.linear_fit[-1] - ds.linear_fit[0])
```
</p> </details>

<details> <summary>Smoothing Data - non-periodic</summary> <p>  

```
%ingrid:
<ds> [time] 1 SM121
```

```
#python:
ds.pad(time=1,mode='symmetric').rolling(time=3, center=True).mean().dropna("time")
```
</p> </details>

<details> <summary>Smoothing Data - periodic</summary> <p>  

```
%ingrid:
<ds> [time] 1 SM121
```

```
#python:
ds.pad(time=1, mode="wrap").rolling(time=3, center=True).mean().dropna("time")
```
</p> </details>

<details> <summary>Root Mean Squared</summary> <p>  

```
%ingrid:
<ds> [time]rmsover
```

```
#python:
ds.std('time')
```
</p> </details>

<details> <summary>Finding Minimum/Maximum</summary> <p>  

```
%ingrid:
<ds> [lon lat] maxover
<ds> [time] minover
```

```
#python:
ds.max(['lon','lat'])
ds.min('time')
```
</p> </details>

<details> <summary>Set minimum/maximum value</summary> <p>  

```
%ingrid:
ds .sst 0 max 28 min
```

```
#python:
ds.sst.clip(min=0,max=28) 
```

</p> </details>

<details> <summary>Mask/Flag Data</summary> <p>  

```
%ingrid:

```

```
#python:
```
</p> </details>

</p> </details>

<details> <summary></summary> <p>  

```
%ingrid:
```

```
#python:
```
</p> </details>

