## Ingrid to Python/Xarray commands

Our beloved `ingrid` methods are becoming obsolete

Help us document equivalent python commands using the [editor on GitHub](https://github.com/naomi-henderson/ingrid2python/edit/main/docs/index.md) to maintain and preview the content of these pages.

<details>
  <summary>1. Grid coarsening </summary>
<p>  

```
#ingrid:
<ds> time 12 boxAverage
```

```
#python:
<ds>.coarsen(time=12,boundary='trim').mean()
# change `.mean()` to `.max()` to get the maximum value in each box
```

</p>
</details>


<details>
  <summary>2. Addition</summary>
<p>  

>ingrid:
```
ds1 ds2 add
```

>python:
```
ds1 + ds2
```

</p>
</details>

