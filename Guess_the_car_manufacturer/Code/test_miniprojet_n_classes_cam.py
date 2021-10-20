import keras
from traitement_images import traitement_images
import time


model = keras.models.load_model("miniprojet_n_classes.h5")

from cv2 import VideoCapture, imwrite


# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
#cam = VideoCapture('http://192.168.1.36:4747/video')



while(1):
   
    s, img = cam.read()
    imwrite("filename.jpg",img)
    while(s == False):
        s, img = cam.read()
        imwrite("filename.jpg",img)
        
    test = traitement_images("filename.jpg")
    res = model.predict(test)
    
    
    if (max(res[0]) == res[0][0]):
        print('BMW [' + "{:.2f}".format(100*res[0][0]) + '%]')
    elif (max(res[0]) == res[0][1]):
        print('Mercedes [' + "{:.2f}".format(100*res[0][1]) + '%]')
    elif (max(res[0]) == res[0][2]):
        print('Audi [' + "{:.2f}".format(100*res[0][2]) + '%]')
        
    else:
        print('Constructeur indéterminé')
    print("[{:.2f}".format(100*res[0][0]) + "%] [{:.2f}".format(100*res[0][1]) + "%] [{:.2f}".format(100*res[0][2]) + "%]")
    
    
    time.sleep(0.3)
    
    print('\n\n\n\n')
  
    
