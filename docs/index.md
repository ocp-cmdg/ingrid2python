## Ingrid to Python/Xarray commands

## Notation

```
<ds> is either an ingrid `stream`(or `Field`) or an xarray `dataset` (or `dataarray`)
<dim> is the name of a dimension/grid (e.g. 'X','lat','time')
<int> is a single integer 
<scalar> is a single real number
<str> is a string
```

further reading: 
- [Xarray Terminology](http://xarray.pydata.org/en/stable/user-guide/terminology.html)
- 

<details>
  <summary>1. Addition/Subtraction/Multiplication </summary>
<p>  
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

</p>
</details>

<details> <summary>2. Grid coarsening </summary> <p>  

```
%ingrid:
 time 12 boxAverage 
```

```
#python:
<ds>.coarsen(time=12,boundary='trim').mean()
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

<details> <summary>5. Averaging over a grid </summary> <p>  

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

