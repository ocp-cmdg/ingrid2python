ingrid:
```
time 12 boxAverage
```


python:
```
.ds.coarsen(time=12,boundary='trim').mean()
```

could change `.mean()` to `.max()` to get the maximum value in each box
