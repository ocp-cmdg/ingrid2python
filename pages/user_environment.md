## Installation Steps:

1. Install your own copy of `conda`:

```
cd ~
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
# read license, accept terms, accept default installation location, let installer run conda init
source ~/.bashrc
```

2. Configure `conda`:

```
conda config --add channels conda-forge --force
conda config --remove channels defaults --force
conda install mamba -y    # use mamba, which is faster than conda
mamba update --all
```

3. Make new environment/kernel:

```
cp /usr/local/python/pangeo.yml .
mamba env create -n my-pangeo -f pangeo.yml
```

4. Add new kernel to your jupyterhub list:

```
conda activate my-pangeo
ipython kernel install --user --name=my-pangeo
conda deactivate
```

### CONGRATULATIONS! - now you can shift-reload your jupyterhub browser page and check it out!

---

## Other useful commands:

- See all of your own environments (kernels):

```
conda activate my-pangeo
jupyter kernelspec list
conda deactivate
```

- Remove this environment:

```
conda activate my-pangeo
jupyter kernelspec uninstall my-pangeo
conda deactivate
```


- See the source code of all of your packages:

```
cd ~/miniconda3/envs/my-pangeo/lib/python3.7/site-packages/
```


- Add a package:

```
conda activate my-pangeo
conda install package-name
conda deactivate
```

- Update/remove a package. Same as above with update(remove) instead of install


- If there is trouble with making a new notebook from the hub, you might need to:
  - kill off all of your notebooks (go to >File >Hub Control Panel  and shutdown hub and then logoff)
  - mv ~/.npm ~/.npm-disable
  - log back into your jupyter notebook
