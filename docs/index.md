## Ingrid to Python/Xarray commands

## Notation
<ds> is either an ingrid `stream` or an xarray `dataset`

<details>
  <summary>1. Addition</summary>
<p>  
In ingrid, compatible objects (streams, numbers) can be added together element by element

```
%ingrid:
<ds1> <ds2> add
```

In python, compatible objects (xarray datasets/dataarrays, numbers) can also be added together
```
#python:
<ds1> + <ds2>
```

</p>
</details>

<details>
  <summary>2. Grid coarsening </summary>
<p>  

```
%ingrid:
<ds> time 12 boxAverage
```

```
#python:
<ds>.coarsen(time=12,boundary='trim').mean()
```
</p>
</details>

