# pycda-crater-detection
Simple code detecting craters on photos from mars.

>update
apt-get update && apt-get upgrade -y

>install git and wget 
apt-get install git wget

>download conda and repo
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
git clone https://github.com/pirokiki/pycda-crater-detection.git

>install anaconda
bash Anaconda3-2022.10-Linux-x86_64.sh

>create virtual environment using conda
conda create -n <name> python=3.6.5

>activate virtual environment
conda activate test

>install pycda and opencv
pip install pycda opencv-python

cd pycda-crater-detection

>make detection script executable
chmod +x craters.py

>run script
./craters.py -f <file name> -s <size in %> -b <blur 1-9>
