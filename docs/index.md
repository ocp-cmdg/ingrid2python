## Ingrid to Python/Xarray commands

## Notation

```
<ds>	: an ingrid `stream`(or `Field`) or an xarray `dataset` (or `dataarray`)
<dim>	: name of a dimension/grid (e.g. 'X','lat','time')
<int>	: integer 
<scalar>: single real number
<str>	: string
<list>  : list of objects (e.g. [2, 'red', (Jan 1950)] )
```

<details> <summary>0. Defining Datasets </summary> <p>  

```
%ingrid:
/ds {(file.nc)readCDF} def
```

```
#python:
ds = xr.open_dataset('file.nc')
```
</p> </details>

<details> <summary>1. Addition/Subtraction/Multiplication </summary> <p>  
In ingrid, compatible objects (streams, numbers) can be added together element by element

```
%ingrid:
<ds1> <ds2> add
```

In python, compatible objects (xarray datasets/dataarrays, numbers) can be added together

```
#python:
<ds1> + <ds2>
```
</p> </details>

<details> <summary>3. Data Selection by grid value </summary> <p>  

```
%ingrid:
<ds> time (Jan 1960) VALUE lat 20 VALUE
```

```
#python:
<ds>.sel(time= '1960-01', lat=20, method='nearest')
```
</p> </details>

<details> <summary>4. Data Selection by grid range </summary> <p>  

```
%ingrid:
<ds> T (Jan 1982) (Dec 1995) RANGE lon 20 60 RANGE
```

```
#python:
<ds>.sel(time=slice('1982-01','1995-12'),lon=slice(20,60))
```
</p> </details>

<details> <summary>5. Averaging over a dimension </summary> <p>  

```
%ingrid:
<ds> [time] average
<ds> [X Y] average
```

```
#python:
<ds>.mean('time')
<ds>.mean(['X','Y'])
```
</p> </details>

<details> <summary>6. Grid coarsening </summary> <p>  

```
%ingrid:
 time 12 boxAverage 
```

```
#python:
<ds>.coarsen(time=12,boundary='trim').mean()
```
</p> </details>

<details> <summary>7. Running Average </summary> <p>  

```
%ingrid:
<ds> time 3 runningAverage
```

```
#python:
<ds>.rolling(time=3, center=True).mean()
```
</p> </details>

