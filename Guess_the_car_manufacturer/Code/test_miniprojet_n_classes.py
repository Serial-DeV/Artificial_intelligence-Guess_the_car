import keras
from traitement_images import traitement_images

model = keras.models.load_model("miniprojet_n_classes.h5")
#Tests

cpt_a = 0
cpt_b = 0
cpt_m = 0
nb_car = 0

rep = '../tests/miniprojet/'

import os

top_dir = os.path.abspath(rep)
files = os.listdir( top_dir )


for i,j in enumerate(files): # i = index, j = nom des fichiers (non triés)
    nb_car += 1
    test = traitement_images(rep + str(i) + '.jpg')
    res = model.predict(test)
    #print(res)
    if (max(res[0]) == res[0][0]):
        print(str(i) + ': BMW [' + "{:.2f}".format(100*res[0][0]) + '%]')
        cpt_b += 1
    elif (max(res[0]) == res[0][1]):
        print(str(i) +': Mercedes [' + "{:.2f}".format(100*res[0][1]) + '%]')
        cpt_m += 1
    elif (max(res[0]) == res[0][2]):
        print(str(i) +': Audi [' + "{:.2f}".format(100*res[0][2]) + '%]')
        cpt_a +=1
        
    else:
        print(str(i) +': Constructeur indéterminé')
    print("[{:.2f}".format(100*res[0][0]) + "%] [{:.2f}".format(100*res[0][1]) + "%] [{:.2f}".format(100*res[0][2]) + "%]")
    print('')
    
print("BMW: " + str(cpt_b) + "/" + str(nb_car))
print("Mercedes: " + str(cpt_m) + "/" + str(nb_car))
print("Audi: " + str(cpt_a) + "/" + str(nb_car))
