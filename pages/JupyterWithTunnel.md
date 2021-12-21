---
title: Ingrid2Python
---

- This allows you to run Jupyter on a REMOTE machine, while using a browser on your LOCAL machine.
- You will need to have a workable `conda` installed on REMOTE, either the system one or your own (see [Installing Conda](https://ocp-cmdg.github.io/ingrid2python/pages/install_conda.html) )
- If you have already been using Jupyter on REMORE, you will have some hidden directories in your home directory which may need to be deleted or renamed.  E.g., `.conda`, `.ipython`, `.jupyter`

# First choose whether you want a Jupyter Notebook, or a Jupyter Lab:

<table>
  <tr><td>1a. Jupyter Notebook</td><td>1b. Jupyter Lab</td></tr>
  <tr><td><img width=500 src="../assets/imgs/JupyterNotebook.png"></td><td><img width=500 src="../assets/imgs/JupyterLab.png"></td></tr>
</table>

# 1a. Jupyter Notebook:
```
# Setup:
conda install jupyter
# Run:
jupyter notebook --no-browser --port=8090
```


# 1b. Jupyter Lab:
```
# Setup on REMOTE:
conda install jupyter
conda install -c conda-forge jupyterlab
jupyter server --generate-config
jupyter server password
# Run on REMOTE:
jupyter lab --no-browser --port=8090 
```
  

# 2. Then start an ssh tunnel on your local machine:
```
# Run on LOCAL:
ssh -N -L 8090:localhost:8090 <user>@<remote>
```

# 3. Point your LOCAL browser (Chrome is good) to http://localhost:8090/


# To see what jupyter processes you have running on REMOTE:
```
jupyter lab list
# or
jupyter notebook list
```


