---
title: Ingrid2Python
---

## Basic Examples

`ds` : an ingrid `stream` or an xarray `dataset`

<details> <summary><b>Getting Started: Defining a Dataset </b></summary> <p>  

[Ingrid on kage](http://kage.ldeo.columbia.edu:81/expert): 


```
%ingrid:

/ds {SOURCES .LOCAL .sst.mon.mean.nc
% Replace the time grid by an 'ingrid-friendly' (but not CF-compliant) time.
time /time (months since 1891-01-01) ordered 0.5 1 1565.5 NewEvenGRID replaceGRID
} def
ds
```

[Python in Jupyter Notebook]()

N.B., You could download the [latest COBE SSTs](ftp://ftp.cdc.noaa.gov/Datasets/COBE/sst.mon.mean.nc') and then open it directly: `xr.open_dataset('sst.mon.mean.nc')`

```
#python:

import xarray as xr
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.sst.mon.mean.nc/.sst/dods'
ds = xr.open_dataset(url)
ds
```
N.B.:  A dataset/stream `ds` can contain multiple variables and grids. A dataarray/field, `da` (for example, ingrid syntax: `ds .sst` and python syntax `ds.sst`) contains a single variable. Most of the commands used in this page can be applied to both datasets and dataarrays. If commands are applied to a dataset, it is applied to all variables in that dataset.

</p> </details>

<details> <summary><b>Selecting Variables and Dimensions</b> </summary> <p>  
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

<details> <summary><b>Basic Plotting</b> </summary> <p>  
In ingrid, click on a plotting thumbnail
    
In python, we can use the built-in `xarray` quick-and-dirty plotting:
    
```
#python:
ds.sst[-1].plot()
```    
But it is nicer to have control over the size and aspect ratio, add titles, etc:

```
#python:
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(8,4))
ds.sst[-1].plot()
plt.title('SSTs of the last month');
```
</p> </details>

<details> <summary><b>Addition/Subtraction/Multiplication</b> </summary> <p>  
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

<details> <summary><b>Data Selection by Grid value</b> </summary> <p>  

```
%ingrid:
ds .sst time (Jan 1960) VALUE lat 20 VALUE
```

```
#python:
ds.sst.sel(time= '1960-01', lat=20, method='nearest').plot()
```
</p> </details>

<details> <summary><b>Data Selection by Grid Range</b> </summary> <p>  

```
%ingrid:
ds T (Jan 1982) (Dec 1995) RANGE lon 20 60 RANGE
```

```
#python:
ds.sel(time=slice('1982-01','1995-12'),lon=slice(20,60))
```
</p> </details>

<details> <summary><b>Averaging over a Dimension</b> </summary> <p>  

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

<details> <summary><b>Grid Coarsening / Box Averaging</b> </summary> <p>  
<a id="Coarsening"/>
    
```
%ingrid:
ds lon 5 boxAverage time 12 boxAverage 
```
- In python we normally use `resample` for time sampling/averaging, but we can use `coarsen` on any grid.

- If the grid is not divisible by the number, use `boundary='trim'`.
    
```
#python:
ds.coarsen(lon=5).mean().coarsen(time=12,boundary='trim').mean()
```
    
For the time grid, here is a `resample` example - note the location of the time values for dsY0 vs. dsY
```
#python
url = 'http://kage.ldeo.columbia.edu:81/SOURCES/.LOCAL/.sst.mon.mean.nc/.sst/dods'
ds = xr.open_dataset(url).mean(['lon','lat']).sel(time=slice('2000','2021'))
dsY0 = ds.resample(time='Y').mean()
dsY = ds.resample(time='Y',label='left',loffset='6M').mean()
ds.sst.plot()
dsY.sst.plot()
dsY0.sst.plot()
```
</p> </details>

<details> <summary><b>Running Average</b> </summary> <p>  

```
%ingrid:
ds .sst time 3 runningAverage
```

```
#python:
ds.sst.rolling(time=3, center=True).mean()
```
</p> </details>

<details> <summary><b>Detrending</b></summary> <p>  

```
%ingrid:
ds .sst [time]detrend-bfl
```

```
#python:
dfit = ds.sst.polyfit('time', 1, skipna=True)
ds.sst - xr.polyval(coord=ds.time, coeffs=dfit.polyfit_coefficients)
```
</p> </details>

<details> <summary><b>Linear Trend</b></summary> <p>  

```
%ingrid:
ds .sst dup [time]detrend-bfl sub dup time last VALUE exch T first VALUE sub
```

```
#python:
dfit = ds.sst.polyfit('time', 1, skipna=True)
ds['linear_fit'] = xr.polyval(coord=ds.time, coeffs=dfit.polyfit_coefficients)
ds['trend'] = (ds.linear_fit[-1] - ds.linear_fit[0])
```
</p> </details>

<details> <summary><b>Smoothing Data - non-periodic</b></summary> <p>  

```
%ingrid:
ds .sst [time] 1 SM121
```

```
#python:
ds.sst.pad(time=1,mode='symmetric').rolling(time=3, center=True).mean().dropna('time')
```
</p> </details>

<details> <summary><b>Smoothing Data - periodic</b></summary> <p>  

```
%ingrid:
ds .sst [time] 1 SM121
```

```
#python:
ds.sst.pad(time=1, mode='wrap').rolling(time=3, center=True).mean().dropna('time')
```
</p> </details>

<details> <summary><b>Root Mean Squared</b></summary> <p>  

```
%ingrid:
ds .sst [time]rmsover
% or, removing the mean first:
ds .sst [time]rmsaover
```

```
#python:
ds.sst.std('time')
# or, removing the mean first:
(ds - ds.mean('time')).sst.std('time')
```
</p> </details>

<details> <summary><b>Finding Minimum/Maximum</b></summary> <p>  

```
%ingrid:
ds .sst [lon lat] maxover
ds .sst [time] minover
```

```
#python:
ds.sst.max(['lon','lat'])
ds.sst.min('time')
```
</p> </details>

<details> <summary><b>Set Minimum/Maximum Value</b></summary> <p>  

```
%ingrid:
ds .sst 0 max 28 min
```

```
#python:
ds.sst.clip(min=0,max=28) 
```

</p> </details>

<details> <summary><b>Mask/Flag Data</b></summary> <p>  

- Masking:

```
%ingrid:
ds .sst 10.0 maskgt
```

```
#python:
ds.sst.where(ds.sst<10)
```

- Flagging:

```
%ingrid:
ds .sst 10.0 flaglt
```

```
#python:
ds.sst.where(ds.sst>10,1.0).where(ds.sst<=10,0.0)
```
</p> </details>

<details> <summary><b>Monthly Climatology</b></summary> <p>  

```
%ingrid:
% time must be called `T`
ds .sst 
time (Jan 1950) (Dec 2019) RANGE
time /T renameGRID yearly-climatology
```

```
#python:
ds.sst.sel(time=slice('1950-01','2019-12')).groupby('time.month').mean()
```
</p> </details>

<details> <summary><b>Monthly Anomalies</b></summary> <p>  

```
%ingrid:
ds .sst 
time (Jan 1950) (Dec 2019) RANGE
time /T renameGRID yearly-anomalies
```

```
#python:
dss = ds.sel(time=slice('1950-01','2019-12'))
dss.sst.groupby('time.month') - dss.sst.groupby('time.month').mean()
```
</p> </details>


<details> <summary><b>Split-Apply-Combine</b></summary> <p>  

```
%ingrid:

ds .sst time 12 splitstreamgrid 
time (Dec) (Jan) (Feb) (Mar) (Apr) VALUES 
[time]average   
```

```
#python:

def is_amj(month):                     # define a function to select the desired months
    return (month >= 12) | (month <= 4)

ds.sst.sel(time=is_amj(ds.sst['time.month'])).groupby('time.year').mean()
```
</p> </details>

<details> <summary><b>Combining Time Segments</b></summary> <p>  

```
%ingrid:
ds .sst time /T renameGRID
  T (Jan 1949) (Dec 1958) RANGE
  yearly-anomalies
ds .sst time /T renameGRID
   T (Jan 1959) (Dec 1978) RANGE
   yearly-anomalies appendstream
ds .sst time /T renameGRID
   T (Jan 1979) (Dec 2001) RANGE
   yearly-anomalies appendstream
```

```
#python:
ds1 = ds.sst.sel(time=slice('1949-01','1958-12'))
ds2 = ds.sst.sel(time=slice('1959-01','1978-12'))
ds3 = ds.sst.sel(time=slice('1979-01','2001-12'))
xr.concat([ds1,ds2,ds3],dim='time')
```
</p> </details>

<details> <summary><b>Standardize a Time Series </b></summary> <p>  

```
%ingrid:
ds .sst 
[time]standardize
```

```
#python:
ds.sst/ds.sst.std('time')
```
</p> </details>

<details> <summary><b>Correlation</b></summary> <p>  

```
%ingrid:
ds .sst time /T renameGRID
  T (Jan 1949) (Dec 2001) RANGE
  yearly-anomalies
dup lon 190 240 RANGE lat -5 5 RANGE [lon lat]average
   [T]correlate
```

```
#python:
dsg = ds.sst.sel(time=slice('1949-01','2001-12')).groupby('time.month')
ds_anom = dsg - dsg.mean()
ds_nino34 = ds_anom.sortby('lat').sel(lon=slice(190,240),lat=slice(-5,5)).mean(['lon','lat'])
xr.corr(ds_anom,ds_nino34,'time')
```
</p> </details>

<details> <summary><b>Regression</b></summary> <p>  

```
%ingrid:
ds .sst time /T renameGRID
  T (Jan 1949) (Dec 2001) RANGE
  yearly-anomalies
dup lon 190 240 RANGE lat -5 5 RANGE [lon lat]average
   [T]standardize
mul [T]average
```

```
#python:
dsg = ds.sst.sel(time=slice('1949-01','2001-12')).groupby('time.month')
ds_anom = (dsg - dsg.mean()).drop('month')
ds_nino34 = ds_anom.sortby('lat').sel(lon=slice(190,240),lat=slice(-5,5)).mean(['lon','lat'])
(ds_anom * ds_nino34/ds_nino34.std('time')).mean('time')
```
</p> </details>

<details> <summary><b>Cosines for Area Weighting </b></summary> <p>  

```
%ingrid:
ds lat cosd
```

```
#python:
coslat = np.cos(np.deg2rad(ds.lat))
```

So we can use this to compute area weighted averages:

```
%ingrid:
ds .sst {lat cosd}[lon lat]weighted-average
```

```
#python:
weights = np.cos(np.deg2rad(ds.lat))
ds.sst.weighted(weights).mean(('lon', 'lat'))
```
</p> </details>

<details> <summary><b>Partial Derivatives</b></summary> <p>  
We prefer to use the `xgcm` package to properly keep track of the grid metrics, but here we use xarray's `differentiate` method since it is similar to ingrid's `partial` method.


```
%ingrid:
ds .sst  a:
    lat partial
    lat :a: .lat REGRID
    :a
  110000. div
```

```
#python:
ds.sst.differentiate('lat')/110000.

```
</p> </details>

<details> <summary><b>Integrals </b></summary> <p>  

```
%ingrid:
ds .sst   a:
    lon integral
    lon :a: .lon REGRID
    :a 
```

```
#python:
ds.sst.cumsum('lon')
```
</p> </details>

<details> <summary><b>Definite Integrals </b></summary> <p>  

```
%ingrid:
ds .sst [lat]average
lon 10 40 definite-integral
```

```
#python:
ds.sst.mean('lat').sel(lon=slice(10,40)).integrate('lon')
```
</p> </details>

<details> <summary><b>Convert daily data to monthly </b></summary> <p>  

```
%ingrid:
SOURCES .LOCAL .tas_day_CESM2_amip_20100101-20150101.nc .tas
time /T renameGRID
monthlyAverage
```

```
#python:    
import xarray as xr

url='http://kage.ldeo.columbia.edu:81/expert/SOURCES/.LOCAL/.tas_day_CESM2_amip_20100101-20150101.nc/.tas/dods'
ds=xr.open_dataset(url,decode_times=True)
ds = tas.sel(time = slice('2010-01-01','2014-12-31'))
ds_monthly = ds.resample(time='1M',label='left',loffset='15D').mean()
```
</p> </details>
    
<details> <summary><b>Save Dataset as a NetCDF File</b></summary> <p>  

```
%ingrid:
SOURCES .LOCAL .tas_day_CESM2_amip_20100101-20150101.nc .tas
time /T renameGRID
monthlyAverage
(tas.mon.mean.nc)writeCDF
```
N.B., `xarray` saves our usual dataset with a time grid that `ingrid` (and `ncview`, etc) will not be able to parse. If you just want to read it back using xr.open_dataset(), that is fine. Otherwise the time grid and the default `encoding` of the netcdf file needs to be changed.
    
```
#python:    
import xarray as xr

url='http://kage.ldeo.columbia.edu:81/expert/SOURCES/.LOCAL/.tas_day_CESM2_amip_20100101-20150101.nc/.tas/dods'
ds=xr.open_dataset(url,decode_times=True)
ds_monthly = ds.resample(time='1M',label='left',loffset='15D').mean()
ds_monthly.to_netcdf('tas.mon.mean.nc')
```
</p> </details>

