---
title: Ingrid2Python
---

## Troubleshooting

<details> <summary><b>Time Grid Trouble</b></summary> <p>  
  
If your dataset, `ds`, is giving trouble with the time grid, `time`,  (as happens frequently), just replace it by a `datetime64` time grid.
  
So here is my crude recipe to replace troublesome time grids with time-centered `datetime64`. Note that there are many variations of frequencies, so please check your time grid after replacement and adjust the recipe accordingly.
  
```
# Replace native time grid by new grid, centered in time
ds=xr.open_dataset('test.nc').resample(time='A').mean()

freq = xr.infer_freq(ds.time)
print(freq)
time = ds['time'] = pd.date_range(str(ds.time.values[0]), periods=len(ds.time), freq=freq)
if 'D' in freq:
    ds['time'] = time.shift(12, freq='H') 
elif 'M' in freq:   
    ds['time'] = time.shift(15, freq='D') 
elif 'A' in freq:
    ds['time'] = time.shift(6, freq='M') 
ds.time  

```
</p> </details> 

[//]: # (This is the beginning.)  

<details> <summary><b>New Entry</b></summary> <p>  
    
```


```
  
</p> </details> 

[//]: # (This is the end.)  
