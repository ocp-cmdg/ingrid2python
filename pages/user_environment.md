## Installation Steps:

1. Install your own copy of `conda`:

```
cd ~
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
# read license, accept terms, accept default installation location, let installer run conda init
source ~/.bashrc
# test to see if python = ~/miniconda3/bin/python
which python
```

2. Configure `conda`:

```
conda config --add channels conda-forge --force
conda config --remove channels defaults --force
conda update --all
```

3. Make new environment/kernel:

```
wget https://raw.githubusercontent.com/ocp-cmdg/ingrid2python/main/assets/pangeo.yml
conda env create -f pangeo.yml
```

4. Add new kernel to your jupyterhub list:

```
conda activate pangeo-Dec2021
ipython kernel install --user --name=pangeo-Dec2021 --display-name pangeo-Dec2021
conda deactivate
```

5. Make another environment/kernel, after modifying pangeo.yml:

    repeat steps 3. and 4. with 'pangeo-Dec2021' replaced by a new name!
    
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
cd ~/miniconda3/envs/pangeo-Dec2021/lib/python3.7/site-packages/
```


- Add a package:

```
conda activate pangeo-Dec2021
conda install package-name
conda deactivate
```

- Update/remove a package. Same as above with update(remove) instead of install


- If you cannot use the jupyterhub interface to add new notebook, you might need to:
  - kill off all of your notebooks (go to >File >Hub Control Panel  and shutdown hub and then logoff)
  - mv ~/.npm ~/.npm-disable
  - log back into your jupyter notebook
