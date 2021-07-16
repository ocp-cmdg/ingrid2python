## Ingrid to Python/Xarray commands

## Notation

```
<ds> is either an ingrid `stream` or an xarray `dataset`
where an ingrid `stream` is a field or number
and an xarray `dataset` is a 
```

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
<ds> time 12 boxAverage
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

