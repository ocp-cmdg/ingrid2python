# Once you have conda, you can start your own Jupyter or JupyterLab

First get the jupyter and/or jupyterlab 
```
conda install jupyter
conda install -c conda-forge jupyterlab
```



#-------------------
#Jupyter Notebook:
#remote:
jupyter notebook --no-browser --port=8090 &
jupyter notebook list
#-------------------

#OR

#-------------------
#Jupyter Lab:
#remote:
jupyter server --generate-config
jupyter server password
jupyter lab --no-browser --port=8090 &
------------------

# Then start an ssh tunnel:
#local:
ssh -N -L 8090:localhost:8090 <user>@<remote>

# and point your browser to:
http://localhost:8090/

