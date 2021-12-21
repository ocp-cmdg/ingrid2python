# Once you have conda, you can start your own Jupyter or JupyterLab

<details> <summary><b>simple Jupyter Notebook</b><p align="center"><img src="../assets/imgs/JupyterNotebook.png"></p></summary>
<p>  
```
# Setup:
conda install jupyter
conda install -c conda-forge jupyterlab
# Run:
jupyter notebook --no-browser --port=8090
```

To see what jupyter notebooks you have running:
```
jupyter notebook list
```
  </p>
  
<details> <summary><b>Jupyter Lab</b><p align="center"><img src="../assets/imgs/JupyterLab.png"></p></summary> 
<p>  
```
# Setup:
conda install -c conda-forge jupyterlab
jupyter server --generate-config
jupyter server password
# Run:
jupyter lab --no-browser --port=8090
```
  </p>
  
  
# Then start an ssh tunnel on your local machine:
```
ssh -N -L 8090:localhost:8090 <user>@<remote>
```

# and point your browser to http://localhost:8090/

