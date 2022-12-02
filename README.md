# Pycda-crater-detection
Simple script detecting craters on photos from mars.

## Update, install git and wget

```
apt-get update && apt-get upgrade -y && apt-get install git wget
```

## Download conda and repo

```
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
git clone https://github.com/pirokiki/pycda-crater-detection.git
```

## Install anaconda

```
bash Anaconda3-2022.10-Linux-x86_64.sh
```

## Create virtual environment using conda

```
conda create -n <name> python=3.6.5
```

## Activate virtual environment

```
conda activate <name>
```

## Install pycda and opencv

```
pip install pycda opencv-python
```

## Make detection script executable

```
cd pycda-crater-detection
chmod +x craters.py
```

## Run script

```
./craters.py -f <file name> -s <size in %> -b <blur 1-9>
```
