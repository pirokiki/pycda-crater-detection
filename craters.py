#!/home/piotr/anaconda3/envs/pycda/bin/python
from pycda import CDA, load_image
import cv2, numpy, subprocess, os, shutil, sys, getopt

#takes args (file and size in %)

opts, args = getopt.getopt(sys.argv[1:], "hf:s:b:", ["help", "file", "size", "blur"])

name = ""
size = ""
blur = ""
for opts, args in opts:
    if opts in ("-h", "--help"):
        print('-f <file> -s <size in %> -b <blur>')
        sys.exit()
    elif opts in ("-f", "--file"):
        name = args
    elif opts in ("-s", "--size"):
        size = args
    elif opts in ("-b", "--blur"):
        blur = args
    else:
        print('-f <file name> -s <size in %> -b <blur 1-9')

#folder creation
if not os.path.exists("backup"):
    os.makedirs("backup")
if not os.path.exists("results"):
    os.makedirs("results")
if not os.path.exists("results_csv"):
    os.makedirs("results_csv")

#locations
location = 'photos/' + name
backup = 'backup/' + name
results = 'results/' + 'plot_' + name

#backup
shutil.copy2(location, backup)

#processing
img = cv2.imread(location, cv2.IMREAD_UNCHANGED) #loading
scale_percent = int(size) #scaling
width = int(img.shape[1] * scale_percent / 100) #scaling
height = int(img.shape[0] * scale_percent / 100) #scaling
dim = (width, height)
imgres = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) #resize
imgbw = cv2.cvtColor(imgres, cv2.COLOR_BGR2GRAY) #grayscale
imggb = cv2.GaussianBlur(imgbw,(int(blur),int(blur)),0)
cv2.imwrite(results, imggb) #saving resized
cda = CDA()
image = load_image(results) #load pre-processed photo
detections = cda.predict(image) #predict craters
prediction = cda.get_prediction(image, verbose=False) #detect craters
#prediction.set_scale(12.5) #skala na wykresie
plot = 'results/' + 'plot_' + name
prediction.show(save_plot=plot)
prediction.to_csv('results_csv/' + 'csv_' + name)
prediction.show()
