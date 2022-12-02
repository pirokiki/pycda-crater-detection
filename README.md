# pycda-crater-detection
Simple code detecting craters on photos from mars.

wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

git clone 

bash Anaconda3-2022.10-Linux-x86_64.sh

conda create -n test python=3.6.5

conda activate test

pip install pycda opencv-python

chmod +x craters.py

./craters.py -f <file name> -s <size in %> -b <blur 1-9>
