## Make Your Own Python Environment/Kernel:

- You will need to have a workable `conda` installed, either the system one or your own (see [Installing Conda](https://) )

1. Make new environment/kernel:

```
wget https://raw.githubusercontent.com/ocp-cmdg/ingrid2python/main/assets/pangeo.yml
# edit pangeo.yml, adding other packages you would like to start with
conda env create -f pangeo.yml -n my-pangeo
```

2. Add new kernel to your jupyter list:

```
conda activate my-pangeo
ipython kernel install --user --name=my-pangeo
conda deactivate
```

3. Make another environment/kernel, after modifying pangeo.yml:

    repeat steps 1. and 2. with 'my-pangeo' replaced by a new name!
    
### CONGRATULATIONS! - now you can shift-reload your jupyterhub browser page and check it out!

---

## Other useful commands:

- See all of your own environments (kernels):

```
jupyter kernelspec list
```

- Remove this environment:

```
jupyter kernelspec uninstall my-pangeo
```

- See the source code of all of your packages:

```
cd ~/miniconda3/envs/my-pangeo/lib/python3.7/site-packages/
```


- Add another package to your kernel:

```
conda activate my-pangeo
conda install package-name
conda deactivate
```

- Update/remove a package from your kernel. Same as above with update(remove) instead of install


- If you cannot use the jupyterhub interface to add new notebook, you might need to:
  - kill off all of your notebooks (go to >File >Hub Control Panel  and shutdown hub and then logoff)
  - mv ~/.npm ~/.npm-disable
  - log back into your jupyter notebook
