---
title: Start Your Own JupyterLab on a Remote Server, Using an 'ssh tunnel' for security
---

## 1. Install Miniconda on Remote Server:


1. Log onto remote machine and then check what shell you are using:
```
echo $SHELL
```
If it is not bash, change to bash

2. Get the miniconda version of conda package manager
```
cd ~
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

3. Install miniconda
```
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

#let it prepend miniconda3 to path, then
source ~/.bashrc
```

4. Test your installation:
```
which python
```
It should be ~/miniconda3/bin/python
