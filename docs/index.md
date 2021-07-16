## Ingrid to Python/Xarray commands

Our beloved `ingrid` methods are becoming obsolete

Help us document equivalent python commands using the [editor on GitHub](https://github.com/naomi-henderson/ingrid2python/edit/main/docs/index.md) to maintain and preview the content of these pages.

[time 12 boxAverage](https://github.com/naomi-henderson/ingrid2python/boxAverage.html)
<details>
  <summary>time 12 boxAverage</summary>
  
```
#ingrid
time 12 boxAverage
```

```
#python
.ds.coarsen(time=12,boundary='trim').mean()
```

could change `.mean()` to `.max()` to get the maximum value in each box
</details>
