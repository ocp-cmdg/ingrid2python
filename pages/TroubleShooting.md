---
title: Ingrid2Python
---

## Troubleshooting

<details> <summary><b>Time Grid Trouble</b></summary> <p>  
  If your dataset, `ds`, is giving trouble with the time grid, `time`,  (as happens frequently), just replace it by a `datetime64` time grid.
  
```
# For daily data
ds['time'] = pd.date_range("2010-01-01", periods=len(ds.time), freq='D')
  
# To put monthly data on a time grid the end of each month
ds['time'] = pd.date_range("2010-01-01", periods=len(ds.time), freq='M')
  
# To put monthly data ont a time grid centered on the 16th of each month
ds['time'] = pd.date_range("2010-01-01", periods=len(ds.time), freq='MS').shift(15, freq='D') 
```
  
</p> </details> 
