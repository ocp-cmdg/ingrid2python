## Installing conda, the python package and environment manager:

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
conda update --all
```
